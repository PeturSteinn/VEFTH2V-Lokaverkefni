
from Database.HotelConnect import *
from time import gmtime, strftime
CustomerList = Customer()
CommonPS = CommonPS()
Reservation=Reservation()
Room=Room()
order_Room=Order_Has_Rooms()


#print(CustomerList.CustomerList())
kust_orders = CommonPS.CustomerOrders(20)
print(kust_orders)
orders = []
print('llb',CommonPS.TotalRoomBill(78))
teljari = 0

for y in kust_orders:
    order = {}
    flokkur = CommonPS.TotalRoomBill(y[teljari]) # mundi skýra order en það er tekið
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
        herbergi['days'] =x[5]
        herbergi['totalprice'] = x[6]
        order['herbergi'].append(herbergi)
        orderprice += int(x[6])
    order['orderprice'] = orderprice
    orders.append(order)



