from ice_cream_shop import IceCreamShop
from ice_cream_factory import ConeMachine, SundaeMachine, MilkshakeMachine

from enum import IntEnum

class DessertOption(IntEnum):
    CONE = 1
    SUNDAE = 2
    MILKSHAKE = 3

DESSERT_FACTORY = {
    DessertOption.CONE: ConeMachine(),
    DessertOption.SUNDAE: SundaeMachine(),
    DessertOption.MILKSHAKE: MilkshakeMachine()
}

if __name__ == "__main__":
    dessert_input = DessertOption(int(
        input("Welcome to the ice-cream shop! What kind of dessert would you like?\n1) Cone\n2) Sundae\n3) Milkshake\n")
    ))
    
    shop = IceCreamShop()
    shop.process_order(DESSERT_FACTORY.get(dessert_input))