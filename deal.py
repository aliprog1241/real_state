from base import BaseClass


class Sell(BaseClass):
    def __init__(self,price_per_meters, discountable, convertable, *args, **kwargs):
        self.price_per_meters = price_per_meters
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

