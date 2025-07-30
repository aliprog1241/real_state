from advertisment import ApartmentSell, ApartmentRent, HouseSell, HouseRent, StoreSell, StoreRent


def creat_sample():
    # ساخت چند نمونه آگهی برای تست

    ApartmentSell(area=80, address="Tehran, Valiasr St", price_per_meters=120000)
    ApartmentSell(area=70, address="Tehran, Enghelab St", price_per_meters=100000)
    ApartmentRent(area=85, address="Tehran, Saadi St", initial_price=10000000, monthly_price=500000)

    HouseSell(area=150, address="Shiraz, Zand St", floors=2, price_per_meters=150000)
    HouseRent(area=120, address="Shiraz, Eram St", floors=1, initial_price=8000000, monthly_price=300000)

    StoreSell(area=50, address="Isfahan, Chahar Bagh", parking=True, price_per_meters=200000)
    StoreRent(area=60, address="Isfahan, Naqsh-e Jahan", parking=False, initial_price=6000000, monthly_price=400000)
