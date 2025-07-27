from random import choice
from user import User
from estate import Apartment,House,Store
from region import Region
from advertisment import ApartmentSell


#creat information for customer

FIRST_NAME = ['Ali', 'Reza', 'mehdi']
LAST_NAME = ['Miri', 'Rezvani', 'Mosavi']
MOBILES = ['09199983035', '09196696504', '09159228564', '09128464401', '09121112334']

#prints information for customer
if __name__ =="__main__":
    for mobile in MOBILES:

        User (choice(FIRST_NAME), choice(LAST_NAME), mobile)
    for user in User.object_list:
        print(f"{user.id}\t {user.fullname}")

    reg1 =Region(name='R1')
    apt1 = Apartment(user= User.object_list[0], area=80, room_count=2, built_year=1380,
    has_elevator=True, has_parking=True, floor=2, region=reg1, address = "shahrak Enghelab" 
     )
    apt1.show_description()

    house = House( has_yard=True, floors_count=2, user= User.object_list[2],
    area = 400, room_count =4, built_year=1345, region=reg1, address = "shahrak Enghelab" 
                  
    )
    house.show_description()

    store = Store(user=User.object_list[-1], area=30, room_count=0, built_year=1399, region=reg1, 
    address="shahrak Enghelab" 

    )
    store.show_description()


    #creat advertisment :

    apartment_sell = ApartmentSell(user= User.object_list[0], area=80, room_count=2, built_year=1380,
    has_elevator=True, has_parking=True, floor=2, region=reg1, address = "shahrak Enghelab" ,
    price_per_meters=10, discountable=True,  convertable=False )

    print(apartment_sell.show_price())