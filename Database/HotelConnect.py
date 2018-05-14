from mysql.connector import MySQLConnection, Error
from .python_mysql_dbconfig import read_db_config


class DbConnector:
    def __init__(self):
        self.db_config = read_db_config()
        self.status = ' '
        try:
            self.conn = MySQLConnection(**self.db_config)
            if self.conn.is_connected():
                self.status = 'OK'
            else:
                self.status = 'connection failed.'
        except Error as error:
            self.status = error

    def execute_function(self, func_header=None, argument_list=None):
        cursor = self.conn.cursor()
        try:
            if argument_list:
                func = func_header % argument_list
            else:
                func = func_header
            cursor.execute(func)
            result = cursor.fetchone()
        except Error as e:
            self.status = e
            result = None
        finally:
            cursor.close()
        return result[0]

    def execute_procedure(self, proc_name, argument_list=None):
        result_list = list()
        cursor = self.conn.cursor()
        try:
            if argument_list:
                cursor.callproc(proc_name, argument_list)
            else:
                cursor.callproc(proc_name)
            self.conn.commit()
            for result in cursor.stored_results():
                result_list = [list(elem) for elem in result.fetchall()]
        except Error as e:
            self.status = e
            print(e)
        finally:
            cursor.close()
        return result_list


class CommonPS(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def HireEmployee(self, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_HotelID, Param_EmpSSN, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Param_ApartNum=None,):
        new_id = 0
        result = self.execute_procedure('EmployeeHire_Bundle', [Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum, Param_HotelID, Param_EmpSSN, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            new_id = int(result[0][0])
        return new_id

    def RegisterCustomer(self, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_CusSSN, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Param_ApartNum=None):
        new_id = 0
        result = self.execute_procedure('CustomerRegister_Bundle', [Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum, Param_CusSSN, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            new_id = int(result[0][0])
        return new_id

    def CheckAvailability(self, New_Start, New_End, Param_HotelID, Param_TypeID):
        result = self.execute_procedure('CheckAvailability', [New_Start, New_End, Param_HotelID, Param_TypeID])
        if result:
            return result
        else:
            return list()

    def TotalServiceBill(self, Param_OrderID):
        result = self.execute_procedure('TotalServiceBill', [Param_OrderID])
        if result:
            return result
        else:
            return list()

    def TotalRoomBill(self, Param_OrderID):
        result = self.execute_procedure('TotalRoomBill', [Param_OrderID])
        if result:
            return result
        else:
            return list()

    def ReservationAdd(self, Param_EmpID, Param_CusID, Param_OrderDate):
        new_id = 0
        result = self.execute_procedure('ReservationAdd', [Param_EmpID, Param_CusID, Param_OrderDate])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ReservationRoomAdd(self, Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate):
        new_id = 0
        print("HotelConnect", Param_CheckInDate)
        print("HotelConnect", Param_CheckOutDate)
        result = self.execute_procedure('ReservationRoomAdd', [Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ServiceOrderAdd(self, Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService):
        new_id = 0
        result = self.execute_procedure('ServiceOrderAdd', [Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService])
        if result:
            new_id = int(result[0][0])
        return new_id


    def ServiceAddItem(self, Param_ServiceID, Param_ItemID, Param_Qty):
        new_id = 0
        result = self.execute_procedure('ServiceAddItem', [Param_ServiceID, Param_ItemID, Param_Qty])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ServiceListOrdersByHotel(self, Param_HotelID):
        result = self.execute_procedure('ServiceListOrdersByHotel', [Param_HotelID])
        if result:
            return result
        else:
            return list()

    def HotelAbout(self):
        result = self.execute_procedure('HotelAbout')
        if result:
            return result
        else:
            return list()

    def GetWorkplaces(self, Param_EmpID):
        result = self.execute_procedure('GetWorkplaces', [Param_EmpID])
        if result:
            return result
        else:
            return list()

    def CustomerOrders(self, Param_CusID):
        result = self.execute_procedure('CustomerOrders', [Param_CusID])
        if result:
            return result
        else:
            return list()

    def RoomsOnOrder(self, Param_OrderID):
        result = self.execute_procedure('RoomsOnOrder', [Param_OrderID])
        if result:
            return result
        else:
            return list()

    def ServicesOnRooms(self, Param_OrderID, Param_RoomID):
        result = self.execute_procedure('ServicesOnRooms', [Param_OrderID, Param_RoomID])
        if result:
            return result
        else:
            return list()

    def ServiceDetails(self, Param_ServiceID):
        result = self.execute_procedure('ServiceDetails', [Param_ServiceID])
        if result:
            return result
        else:
            return list()

    def ServiceItemDetails(self, Param_OrderItemID):
        result = self.execute_procedure('ServiceItemDetails', [Param_OrderItemID])
        if result:
            return result
        else:
            return list()


class Address(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def AddressAdd(self, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum=None, Address_NewID=None):
        new_id = 0
        result = self.execute_procedure('AddressAdd', [Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum, Address_NewID])
        if result:
            new_id = int(result[0][0])
        return new_id

    def AddressList(self):
        result = self.execute_procedure('AddressList')
        if result:
            return result
        else:
            return list()

    def AddressInfo(self, Param_AddressID):
        result = self.execute_procedure('AddressInfo', [Param_AddressID])
        if result:
            return result
        else:
            return list()

    def AddressUpdate(self, Param_AddressID, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum=None):
        rows_affected = 0
        result = self.execute_procedure('AddressUpdate', [Param_AddressID, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def AddressDelete(self, Param_AddressID):
        rows_affected = 0
        result = self.execute_procedure('AddressDelete', [Param_AddressID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Customer(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def CustomerAdd(self, Param_CusSSN, Param_AddressID, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass):
        new_id = 0
        result = self.execute_procedure('CustomerAdd', [Param_CusSSN, Param_AddressID, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            new_id = int(result[0][0])
        return new_id

    def CustomerList(self):
        result = self.execute_procedure('CustomerList')
        if result:
            return result
        else:
            return list()

    def CustomerInfo(self, Param_CusID):
        result = self.execute_procedure('CustomerInfo', [Param_CusID])
        if result:
            return result
        else:
            return list()

    def CustomerUpdate(self, Param_CusID, Param_CusSSN, Param_AddressID, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass):
        rows_affected = 0
        result = self.execute_procedure('CustomerUpdate', [Param_CusID, Param_CusSSN, Param_AddressID, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def CustomerDelete(self, Param_CusID):
        rows_affected = 0
        result = self.execute_procedure('CustomerDelete', [Param_CusID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Employee(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def EmployeeAdd(self, Param_EmpSSN, Param_AddressID, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Employee_NewID=None):
        new_id = 0
        result = self.execute_procedure('EmployeeAdd', [Param_EmpSSN, Param_AddressID, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Param_NewID])
        if result:
            new_id = int(result[0][0])
        return new_id

    def EmployeeList(self):
        result = self.execute_procedure('EmployeeList')
        if result:
            return result
        else:
            return list()

    def EmployeeInfo(self, Param_EmpID):
        result = self.execute_procedure('EmployeeInfo', [Param_EmpID])
        if result:
            return result
        else:
            return list()

    def EmployeeUpdate(self, Param_EmpID, Param_EmpSSN, Param_AddressID, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass):
        rows_affected = 0
        result = self.execute_procedure('EmployeeUpdate', [Param_EmpID, Param_EmpSSN, Param_AddressID, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def EmployeeDelete(self, Param_EmpID):
        rows_affected = 0
        result = self.execute_procedure('EmployeeDelete', [Param_EmpID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Hotel(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def HotelAdd(self, Param_AddressID, Param_HotelName):
        new_id = 0
        result = self.execute_procedure('HotelAdd', [Param_AddressID, Param_HotelName])
        if result:
            new_id = int(result[0][0])
        return new_id

    def HotelList(self):
        result = self.execute_procedure('HotelList')
        if result:
            return result
        else:
            return list()

    def HotelInfo(self, Param_HotelID):
        result = self.execute_procedure('HotelInfo', [Param_HotelID])
        if result:
            return result
        else:
            return list()

    def HotelUpdate(self, Param_HotelID, Param_AddressID, Param_HotelName):
        rows_affected = 0
        result = self.execute_procedure('HotelUpdate', [Param_HotelID, Param_AddressID, Param_HotelName])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def HotelDelete(self, Param_HotelID):
        rows_affected = 0
        result = self.execute_procedure('HotelDelete', [Param_HotelID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Item(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def ItemAdd(self, Param_ItemName, Param_ItemDetails, Param_Cost):
        new_id = 0
        result = self.execute_procedure('ItemAdd', [Param_ItemName, Param_ItemDetails, Param_Cost])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ItemList(self):
        result = self.execute_procedure('ItemList')
        if result:
            return result
        else:
            return list()

    def ItemInfo(self, Param_ItemID):
        result = self.execute_procedure('ItemInfo', [Param_ItemID])
        if result:
            return result
        else:
            return list()

    def ItemUpdate(self, Param_ItemID, Param_ItemName, Param_ItemDetails, Param_Cost):
        rows_affected = 0
        result = self.execute_procedure('ItemUpdate', [Param_ItemID, Param_ItemName, Param_ItemDetails, Param_Cost])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def ItemDelete(self, Param_ItemID):
        rows_affected = 0
        result = self.execute_procedure('ItemDelete', [Param_ItemID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Reservation(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def ReservationAdd(self, Param_EmpID, Param_CusID, Param_OrderDate):
        new_id = 0
        result = self.execute_procedure('ReservationAdd', [Param_EmpID, Param_CusID, Param_OrderDate])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ReservationList(self):
        result = self.execute_procedure('ReservationList')
        if result:
            return result
        else:
            return list()

    def ReservationInfo(self, Param_OrderID):
        result = self.execute_procedure('ReservationInfo', [Param_OrderID])
        if result:
            return result
        else:
            return list()

    def ReservationUpdate(self, Param_OrderID, Param_EmpID, Param_CusID, Param_OrderDate):
        rows_affected = 0
        result = self.execute_procedure('ReservationUpdate', [Param_OrderID, Param_EmpID, Param_CusID, Param_OrderDate])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def ReservationDelete(self, Param_OrderID):
        rows_affected = 0
        result = self.execute_procedure('ReservationDelete', [Param_OrderID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Order_Has_Items(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def ServiceAddItem(self, Param_ServiceID, Param_ItemID, Param_Qty):
        new_id = 0
        result = self.execute_procedure('ServiceAddItem', [Param_ServiceID, Param_ItemID, Param_Qty])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ServiceListItems(self):
        result = self.execute_procedure('ServiceListItems')
        if result:
            return result
        else:
            return list()

    def ServiceInfoItems(self, Param_OrderItemID):
        result = self.execute_procedure('ServiceInfoItems', [Param_OrderItemID])
        if result:
            return result
        else:
            return list()

    def ServiceUpdateItem(self, Param_OrderItemID, Param_ServiceID, Param_ItemID, Param_Qty):
        rows_affected = 0
        result = self.execute_procedure('ServiceUpdateItem', [Param_OrderItemID, Param_ServiceID, Param_ItemID, Param_Qty])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def ServiceDeleteItem(self, Param_OrderItemID):
        rows_affected = 0
        result = self.execute_procedure('ServiceDeleteItem', [Param_OrderItemID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Order_Has_Rooms(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def ReservationRoomAdd(self, Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate):
        new_id = 0
        result = self.execute_procedure('ReservationRoomAdd', [Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ReservationRoomList(self):
        result = self.execute_procedure('ReservationRoomList')
        if result:
            return result
        else:
            return list()

    def ReservationRoomInfo(self, Param_OrderRoomID):
        result = self.execute_procedure('ReservationRoomInfo', [Param_OrderRoomID])
        if result:
            return result
        else:
            return list()

    def ReservationRoomUpdate(self, Param_OrderRoomID, Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate):
        rows_affected = 0
        result = self.execute_procedure('ReservationRoomUpdate', [Param_OrderRoomID, Param_OrderID, Param_RoomID, Param_CheckInDate, Param_CheckOutDate])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def ReservationDelete(self, Param_OrderRoomID):
        rows_affected = 0
        result = self.execute_procedure('ReservationDelete', [Param_OrderRoomID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Room(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def RoomAdd(self, Param_HotelID, Param_TypeID, Param_DoorNum):
        new_id = 0
        result = self.execute_procedure('RoomAdd', [Param_HotelID, Param_TypeID, Param_DoorNum])
        if result:
            new_id = int(result[0][0])
        return new_id

    def RoomList(self):
        result = self.execute_procedure('RoomList')
        if result:
            return result
        else:
            return list()

    def RoomInfo(self, Param_RoomID):
        result = self.execute_procedure('RoomInfo', [Param_RoomID])
        if result:
            return result
        else:
            return list()

    def RoomUpdate(self, Param_RoomID, Param_HotelID, Param_TypeID, Param_DoorNum):
        rows_affected = 0
        result = self.execute_procedure('RoomUpdate', [Param_RoomID, Param_HotelID, Param_TypeID, Param_DoorNum])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def RoomDelete(self, Param_RoomID):
        rows_affected = 0
        result = self.execute_procedure('RoomDelete', [Param_RoomID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class RoomType(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def RoomTypeAdd(self, Param_RoomType, Param_Desc, Param_Cost):
        new_id = 0
        result = self.execute_procedure('RoomTypeAdd', [Param_RoomType, Param_Desc, Param_Cost])
        if result:
            new_id = int(result[0][0])
        return new_id

    def RoomTypeList(self):
        result = self.execute_procedure('RoomTypeList')
        if result:
            return result
        else:
            return list()

    def RoomTypeInfo(self, Param_TypeID):
        result = self.execute_procedure('RoomTypeInfo', [Param_TypeID])
        if result:
            return result
        else:
            return list()

    def RoomTypeUpdate(self, Param_TypeID, Param_RoomType, Param_Desc, Param_Cost):
        rows_affected = 0
        result = self.execute_procedure('RoomTypeUpdate', [Param_TypeID, Param_RoomType, Param_Desc, Param_Cost])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def RoomTypeDelete(self, Param_TypeID):
        rows_affected = 0
        result = self.execute_procedure('RoomTypeDelete', [Param_TypeID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class ServiceOrder(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def ServiceOrderAdd(self, Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService):
        new_id = 0
        result = self.execute_procedure('ServiceOrderAdd', [Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService])
        if result:
            new_id = int(result[0][0])
        return new_id

    def ServiceOrderList(self):
        result = self.execute_procedure('ServiceOrderList')
        if result:
            return result
        else:
            return list()

    def ServiceOrderInfo(self, Param_ServiceID):
        result = self.execute_procedure('ServiceOrderInfo', [Param_ServiceID])
        if result:
            return result
        else:
            return list()

    def ServiceOrderUpdate(self, Param_ServiceID, Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService):
        rows_affected = 0
        result = self.execute_procedure('ServiceOrderUpdate', [Param_ServiceID, Param_RoomID, Param_OrderID, Param_EmpID, Param_DateTimeOfService])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def ServiceOrderDelete(self, Param_ServiceID):
        rows_affected = 0
        result = self.execute_procedure('ServiceOrderDelete', [Param_ServiceID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

class Staff(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def StaffAdd(self, Param_EmpID, Param_HotelID):
        new_id = 0
        result = self.execute_procedure('StaffAdd', [Param_EmpID, Param_HotelID])
        if result:
            new_id = int(result[0][0])
        return new_id

    def StaffList(self):
        result = self.execute_procedure('StaffList')
        if result:
            return result
        else:
            return list()

    def StaffInfo(self, Param_StaffID):
        result = self.execute_procedure('StaffInfo', [Param_StaffID])
        if result:
            return result
        else:
            return list()

    def StaffUpdate(self, Param_StaffID, Param_EmpID, Param_HotelID):
        rows_affected = 0
        result = self.execute_procedure('StaffUpdate', [Param_StaffID, Param_EmpID, Param_HotelID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def StaffDelete(self, Param_StaffID):
        rows_affected = 0
        result = self.execute_procedure('StaffDelete', [Param_StaffID])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected
