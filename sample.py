from random import choice
from user import User
from estate import Apartment, House, Store
from region import Region
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent

#creat information for customer

FIRST_NAME = ['Ali', 'Reza', 'mehdi']
LAST_NAME = ['Miri', 'Rezvani', 'Mosavi']
MOBILES = ['09199983035', '09196696504', '09159228564', '09128464401', '09121112334']

#prints information for customer
def creat_sample():
    for mobile in MOBILES:
        User (choice(FIRST_NAME), choice(LAST_NAME), mobile)

    # for user in User.objects_list:
    #     print(f"{user.id}\t {user.fullname}")




    reg1 = Region(name='R1')
    # reg2 =Region(name='R2')

    apt1 = Apartment(user= User.objects_list[0], area=80, room_count=2, built_year=1380,
                     has_elevator=True, has_parking=True, floor=2, region=reg1, address = "shahrak Enghelab"
                     )
    # apt1.show_description()

    house = House(has_yard=True, floors_count=2, user= User.objects_list[2],
                  area = 400, room_count =4, built_year=1345, region=reg1, address = "shahrak Enghelab"

                  )
    # house.show_description()

    store = Store(user=User.objects_list[-1], area=30, room_count=0, built_year=1399, region=reg1,
                  address="shahrak Enghelab"

                  )
    # store.show_description()


    #creat advertisement

    apartment_sell = ApartmentSell(
        user=User.objects_list[0], area=80, room_count=2, built_year=1380, region=reg1, address="shahrak Enghelab",
        has_elevator=True, has_parking=True, floor=2, price_per_meters=10, discountable=True, convertable=False
    )

    # apartment_sell.show_detail()

    apartment_rent = ApartmentRent(user=User.objects_list[0], area=80, room_count=2, built_year=1380, region=reg1, address="shahrak Enghelab",
        has_elevator=True, has_parking=True, floor=2, convertable=False,initial_price=100, monthly_price=30 ,

    )

    house_rent = HouseRent(has_yard=True, floors_count=2, user=User.objects_list[2],
        area=400, room_count=4, built_year=1345, region=reg1, address="shahrak Enghelab",
        convertable=False,initial_price=300, monthly_price=10

    )

    house_sell = HouseSell(
        has_yard=True, floors_count=2, user=User.objects_list[2],
        area=400, room_count=4, built_year=1345, region=reg1, address="shahrak Enghelab",
        price_per_meters=10, discountable=True, convertable=False
    )


    print("#" * 20, "\t sample crate\t ", "#" * 20)

    # house_sell.show_detail()
#
#
# print("result:", ApartmentSell.manager.search(region=reg1))
# print("result:", ApartmentSell.manager.search(room_count=2))
# print("result price:", ApartmentSell.manager.search(price_per_meters__max=8))
#
#
# print("result:", HouseSell.manager.search(region=reg1))
# print("result:", HouseSell.manager.search(floor_count=2))
#
