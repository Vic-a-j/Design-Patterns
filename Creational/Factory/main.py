from ice_cream_factory import DessertMachineFactory, ConeMachine, SundaeMachine, MilkshakeMachine

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

# ============================================================
# Client
# ============================================================

class IceCreamShop:
    """
    The client works with an *abstract* factory of a single product.
    """

    def __init__(self, factory: DessertMachineFactory):
        self.factory = factory

    def process_order(self) -> None:
        """Process orders given desert machine.
        
        Note: The client doesn't know about how to create the order, it simply makes it.
        """
        self.factory.make_order()


if __name__ == "__main__":
    dessert = DessertOption(
        int(
            input("Welcome to the ice-cream shop! What kind of dessert would you like?\n1) Cone\n2) Sundae\n3) Milkshake\n")
        )
    )
    
    shop = IceCreamShop(DESSERT_FACTORY[dessert])
    shop.process_order()