from sample import creat_sample
from advertisment import ApartmentSell, ApartmentRent, HouseSell, HouseRent, StoreSell, StoreRent

class Handler:
    ADVERTISEMENT_TYPS = {
        ApartmentSell, ApartmentRent,
        HouseSell, HouseRent,
        StoreSell, StoreRent,
    }
    SWITCHES = {
        'r': "get_report",
        's': "show_all"
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPS:
            print(f"{adv.__name__}: {adv.manager.count()} ads")

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPS:
            print(f"\n{adv.__name__}: {adv.manager.count()} ads")
            for obj in adv.objects_list:
                obj.show_detail()

    def run(self):
        print("####################     sample crate     ####################")
        print("hello yasin")
        for key, method_name in self.SWITCHES.items():
            print(f"press {key} for {method_name}")
        choice = input("enter your choice: ").strip().lower()

        if choice in self.SWITCHES:
            method = getattr(self, self.SWITCHES[choice])
            method()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    creat_sample()
    handler = Handler()
    handler.run()
