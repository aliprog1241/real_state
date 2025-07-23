from random import choice
from user import User

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
