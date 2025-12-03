from ice_cream_factory import DessertMachineFactory
from ice_cream_products import Dessert

class IceCreamShop():
    def __init__(self):
        pass

    def process_order(self, dessert_machine: DessertMachineFactory) -> Dessert:
        """Process orders given desert machine.
        
        Note: The client doesn't know about how to create the order. It simply makes a dessert.
        """
        dessert_machine.make_order()