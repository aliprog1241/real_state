from base import BaseClass

#reseive firstname,lastname and phone number of customer

class User(BaseClass):
    def __init__(self, first_name, last_name , phone_number,  *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)


    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"