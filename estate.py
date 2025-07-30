class Apartment:
    def __init__(self, area, address, *args, **kwargs):
        self.area = area
        self.address = address
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"Apartment - Area: {self.area} sqm, Address: {self.address}")

class House:
    def __init__(self, area, address, floors, *args, **kwargs):
        self.area = area
        self.address = address
        self.floors = floors
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"House - Area: {self.area} sqm, Address: {self.address}, Floors: {self.floors}")

class Store:
    def __init__(self, area, address, parking, *args, **kwargs):
        self.area = area
        self.address = address
        self.parking = parking
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"Store - Area: {self.area} sqm, Address: {self.address}, Parking: {self.parking}")
