from ice_cream_factory import DessertMachineFactory
from ice_cream_products import Dessert

class IceCreamShop():
    def __init__(self):
        pass

    def process_order(self, dessert_machine: DessertMachineFactory) -> Dessert:
        dessert_machine.make_order()