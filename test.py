from bottle import *
from beaker.middleware import SessionMiddleware
from Database.HotelConnect import *
from time import gmtime, strftime
Customer = Customer()
CommonPS = CommonPS()
Reservation=Reservation()
Room=Room()
order_Room=Order_Has_Rooms()

order_went_through = False
error = ''

Common = CommonPS()
Customer = Customer()
Address = Address()

# Upsetning á hótelum
result = Common.HotelAbout()
hotels = list()
for i in result:
    item = dict()
    item['name'] = i[2]
    item['postcode'] = i[4]
    item['folder'] = i[5].lower()
    item['border'] = str(i[5].lower() + '.jpg')
    hotels.append(item)
for i in hotels:
    print(i)

cookei = ['account', 'fname', 'lname', 'SSN', 'phone', 'mail', 'checkin', 'checkout', 'herbegi','Hotel']


cookei = ['account', 'fname', 'lname', 'SSN', 'phone', 'mail', 'checkin', 'checkout', 'herbegi']
account = {'user':'nonni2000','passwd':'nonni','fname':'Nonni','lname':'Manni','SSN':'4567892345','simi':'5678903','mail':'manni@gmail.com'}

@route('/')
def index():
    global order_went_through
    check_order_went_through = order_went_through
    order_went_through = False
    for x in cookei:
        response.set_cookie('{}'.format(x), "", expires=0)
    return template('views/index', order=check_order_went_through)

@route('/Hotel/<hotelid>')
def index_hotel(hotelid):
    for x in cookei:
        response.set_cookie('{}'.format(x), "", expires=0)
    response.set_cookie('account', "", expires=0)
    for x in hotels:
        print(x)
        print('{}---{}'.format(x['name'],hotelid))
        if x['name']==hotelid:
            temp_hotel = x

    return template('views/index-hotel', hotel=temp_hotel)

@route('/<hotelid>')
def order(hotelid):
    if hotelid == 'Reykavik' or hotelid == 'Selfoss' or hotelid == 'Akureyri':
        checkin = request.query.checkin
        checkout = request.query.ckeckout
        herbegi = request.query.Herbergi
        response.set_cookie('checkin', checkin, secret='my_secret_code')
        response.set_cookie('checkout', checkout, secret='my_secret_code')
        response.set_cookie('herbegi', herbegi, secret='my_secret_code')
        response.set_cookie('Hotel', hotelid, secret='my_secret_code')
        return redirect('/Hotel/order')
    else:
        return 'error'


@route('/Hotel/order')
def orderroom():
    global error
    user = request.get_cookie('account', secret='my_secret_code')
    villa = error
    error=''
    if (user):
        fname = request.get_cookie('fname', secret='my_secret_code')
        lname = request.get_cookie('lname', secret='my_secret_code')
        ssn = request.get_cookie('SSN', secret='my_secret_code')
        phone = request.get_cookie('phone', secret='my_secret_code')
        mail = request.get_cookie('mail', secret='my_secret_code')
        user = {'name':user,'fname':fname,'lname':lname,'ssn':ssn,'phone':phone,'mail':mail}
        ifuser = True
    else:
        ifuser =False

    checkin = request.get_cookie('checkin', secret='my_secret_code')
    checkout = request.get_cookie('checkout', secret='my_secret_code')
    herbergi = request.get_cookie('herbegi', secret='my_secret_code')
    hotelid = request.get_cookie('Hotel', secret='my_secret_code')

    herbergi_uppl = {'checkin':checkin,'checkout':checkout,'herbergi':herbergi,'Hotel':hotelid}
    print(herbergi_uppl)

    return template('order', villa= villa,user=user, herbergi_uppl=herbergi_uppl,ifuser=ifuser)

@route('/login', method='post')
def login():
    customerlist = Customer.CustomerList()

    username = request.forms.get('user')
    password = request.forms.get('password')
    for x in customerlist:
        if username == x[7] and password == x[8]:
            response.set_cookie('account', x[7], secret='my_secret_code')
            response.set_cookie('fname', x[4], secret='my_secret_code')
            response.set_cookie('lname',x[3], secret='my_secret_code')
            response.set_cookie('SSN', x[1], secret='my_secret_code')
            response.set_cookie('phone', x[6], secret='my_secret_code')
            response.set_cookie('mail', x[5], secret='my_secret_code')
            return redirect('/Hotel/order')
    global error
    error = 'Vitlaust lykilorð eða password'
    return redirect('/Hotel/order')



@route('/checkorder', method='post')
def klaraorder():


    ssn = request.forms.get('ssn')
    hotel = request.forms.get('hotel')
    Guset = request.forms.get('Guset')
    Suites = request.forms.get('Suites')
    Executive = request.forms.get('Executive')
    checkin = request.forms.get('checkin')
    checkout = request.forms.get('checkout')
    options = [ssn, hotel, Guset, Suites, Executive, checkin, checkout]
    Guset = int(Guset)
    Suites = int(Suites)
    Executive = int(Executive)


    for x in options:
        if x == "None":
            aframm = False
            break
        else:
            aframm = True

    if aframm:
        print(checkin)
        global error
        # New_Start, New_End, Param_HotelID, Param_TypeID):
        all_cust =Customer.CustomerList()
        for x in all_cust:#hérna er fundið user idið
            if ssn == x[1]:
                user_ID = x[0]
        else:
            pass
            # ef nondani er ekki til

        # búa til pöntun
        datetime = (strftime("%Y-%m-%d %H:%M:%S", gmtime()))# fá dagsetinguna þegar það var pantað
        res_id = Reservation.ReservationAdd(1,user_ID, datetime)# 1= Id hjá strafsmanni sem er vefsíðan

        lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 3))
        if len(lausherbergi) < Guset:
            error = "Það eru ekki nó og mörg laus Guest herbergi"
            redirect('/Hotel/order')

        lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 2))
        if len(lausherbergi) < Suites:
            error = "Það eru ekki nó og mörg laus Suites herbergi"
            redirect('/Hotel/order')

        lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 1))
        if len(lausherbergi) < Executive:
            error = "Það eru ekki nó og mörg laus Executive herbergi"
            redirect('/Hotel/order')


        if Guset > 0:
            #(self, Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate):
            for x in range(Guset):
                lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 3))
                order_Room.ReservationRoomAdd(res_id,lausherbergi[x][0], checkin, checkout) # lausherbergi[x][0] er id af lauasa herberginu.
        else:
            pass
        if Suites > 0:
            for x in range(Suites):
                lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 2))
                order_Room.ReservationRoomAdd(res_id,lausherbergi[x][0], checkin, checkout)# lausherbergi[x][0] er id af lauasa herberginu.
        else:
            pass
        if Executive > 0:
            for x in range(Executive):
                lausherbergi = (CommonPS.CheckAvailability(checkin, checkout, hotel, 1))
                order_Room.ReservationRoomAdd(res_id,lausherbergi[x][0], checkin, checkout) # lausherbergi[x][0] er id af lauasa herberginu.
        else:
            pass

    else:
        pass # senda til backa með villu
    for x in cookei:
        response.set_cookie('{}'.format(x), "", expires=0)
    global order_went_through
    order_went_through = True
    print(res_id)
    return redirect('/')

@route('/bokun' , method='post')
def bokun():
    customerlist = Customer.CustomerList()

    username = request.forms.get('user')
    password = request.forms.get('password')
    for x in customerlist:
        if username == x[7] and password == x[8]:
            response.set_cookie('account', x[7], secret='my_secret_code')
            response.set_cookie('accountID', x[0], secret='my_secret_code')
    else:
        global error
        error = 'vilaust notandanafn eða lykilorð'
        return redirect('/bokun')


@route('/bokun')
def bokun():
    accountID = request.get_cookie('accountID', secret='my_secret_code')
    account = request.get_cookie('account', secret='my_secret_code')
    global error
    villa = error
    error = ''
    teljari = 0
    if (account):
        kust_orders = CommonPS.CustomerOrders(accountID)
        orders=[]
        for y in kust_orders:
            order = {}
            flokkur = CommonPS.TotalRoomBill(y[teljari])  # mundi skýra order en það er tekið
            orderprice = 0
            order['hotel'] = flokkur[0][7]
            for x in flokkur:
                order['checkin'] = x[0]
                order['checkout'] = x[1]
                order['herbergi'] = []
                herbergi = {}
                herbergi['type'] = x[2]
                herbergi['nuber'] = x[3]
                herbergi['price'] = x[4]
                herbergi['days'] = x[5]
                herbergi['totalprice'] = x[6]
                order['herbergi'].append(herbergi)
                orderprice += int(x[6])
            order['orderprice'] = orderprice
            orders.append(order)
    print(orders)
    return template('tabel', villa=villa, user= account, orders=orders)


@route('/signup' , method='post')
def signup():
    customerlist = Customer.CustomerList()

    username = request.forms.get('user')
    password = request.forms.get('password')
    for x in customerlist:
        if username == x[7]:
            global error
            error = 'Notandanafn tekið'
            return redirect('/hotel/order')
    user = request.forms.get('user')
    password = request.forms.get('password')
    fname = request.forms.get('fname')
    lname = request.forms.get('lname')
    ssn = request.forms.get('ssn')
    mail = request.forms.get('mail')
    phone = request.forms.get('phone')
    CountryName = request.forms.get('CountryName')
    CityName = request.forms.get('CityName')
    StreetName = request.forms.get('StreetName')
    Zip = request.forms.get('Zip')
    BuildingNum = request.forms.get('BuildingNum')
    ApartNum = request.forms.get('ApartNum')
    if ApartNum == None:
        CommonPS.RegisterCustomer(Zip,CityName,CountryName,StreetName,BuildingNum,ssn,lname,fname,mail,phone,user,password,ApartNum)
    else:
        CommonPS.RegisterCustomer(Zip, CityName, CountryName, StreetName, BuildingNum, ssn, lname, fname, mail, phone,
                                  user, password)


    return redirect('/Hotel/order')


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

session_options = {
    'session.type': 'file',
    'session.data_dir':'./data'
}

my_session = SessionMiddleware(app(), session_options)

run(host='localhost', port='8080', debug='True', reloader='True')
