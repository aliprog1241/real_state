from random import choice

from sample import creat_sample
from advertisment import ApartmentSell, ApartmentRent, HouseSell, HouseRent, StoreSell, StoreRent

class Handler:
   ADVERTISEMENT_TYPS = {
      1: ApartmentSell, 2: ApartmentRent,
      3: HouseSell, 4: HouseRent,
      5: StoreSell, 6: StoreRent,

   }
   SWITCHES = {

      'r':"get_report",
      's':"show_all"
   }

   def run(self):
      print("hello world!")
      for key in self.SWITCHES.items():
         print(f"press {key} for {self.SWITCHES[key]}")
      choice = input("inter your choice: ")

#prints information for customer
if __name__ =="__main__":
   creat_sample()
   handler = Handler()

   handler.run()