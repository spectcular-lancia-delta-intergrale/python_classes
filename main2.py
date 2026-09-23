import random

Basic_Items = ["Shotgun", "Handgun", "Rifle", "Pistol", "Sword", "PenKnife","Axe"]

class Inventory:
    def __init__(self):
        bckpck = [] * 10
        self.bckpck = bckpck
    def add_invent_item(self, item):
        if self.bckpck.count(item) < 10:
            self.bckpck.append(item)
    def remove_invent_item(self, item):
        if self.bckpck.count(item) > 0:
            self.bckpck.remove(item)
    def showcase_invent(self):
        print(f"Inventory: {self.bckpck}")


Player1 = Inventory()
Player1.add_invent_item(Basic_Items[random.randint(0, len(Basic_Items)-1)])
Player1.showcase_invent()


