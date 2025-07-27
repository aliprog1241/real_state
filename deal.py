from base import BaseClass
from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meters, discountable, convertable, *args, **kwargs):
        self.price_per_meters = price_per_meters
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)


    def show_price(self):
        print(f"price : {self.price_per_meters}\t discount: {self.discountable}\t convertable: {self.convertable}")




class Rent(ABC):
    def __init__(self, initial_price, monthly_price, convertable, discountable, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)
