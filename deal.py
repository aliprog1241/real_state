from abc import ABC

class Sell(ABC):
    def __init__(self, price_per_meters, discountable=True, convertable=False, *args, **kwargs):
        self.price_per_meters = price_per_meters
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"Price: {self.price_per_meters}, Discountable: {self.discountable}, Convertable: {self.convertable}")

class Rent(ABC):
    def __init__(self, initial_price, monthly_price, convertable=False, discountable=False, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"Initial Price: {self.initial_price}, Monthly Price: {self.monthly_price}, Convertable: {self.convertable}, Discountable: {self.discountable}")
