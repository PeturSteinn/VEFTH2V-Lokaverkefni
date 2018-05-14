
from Database.HotelConnect import *
from time import gmtime, strftime
CustomerList = Customer()
CommonPS = CommonPS()
Reservation=Reservation()
Room=Room()
order_Room=Order_Has_Rooms()


#print(CustomerList.CustomerList())
kust_orders = CommonPS.CustomerOrders(21)
print(kust_orders)
orders = []
print('llb',CommonPS.TotalRoomBill(78))
teljari = 0

for y in kust_orders:
    order = {}
    flokkur = CommonPS.TotalRoomBill(y[0]) # mundi skýra order en það er tekið
    orderprice = 0
    order['hotel'] = flokkur[0][7]
    order['herbergi'] = []
    for x in flokkur:
        herbergi = {}
        order['checkin'] = x[0]
        order['checkout'] = x[1]
        herbergi['type'] = x[2]
        herbergi['nuber'] = x[3]
        herbergi['price'] = x[4]
        herbergi['days'] =x[5]
        herbergi['totalprice'] = x[6]
        print(herbergi)
        order['herbergi'].append(herbergi)
        orderprice += int(x[6])
    order['orderprice'] = orderprice
    print(order)
    orders.append(order)
print('''''')
for x in orders:
    print(x['herbergi'])



