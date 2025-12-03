from abc import ABC, abstractmethod

from ice_cream_products import Dessert, Sundae, Cone, Milkshake

# -------------------------------------
# Creator (Factory)
#
# Note: The factory here creates the dessert, the subclasses only know what kind of dessert.
# -------------------------------------
class DessertMachineFactory(ABC):
    @abstractmethod
    def create_dessert(self) -> Dessert:
        """Abstract class to create dessert."""
        pass

    def make_order(self) -> Dessert:
        """Delegates dessert creation to the subclass."""
        dessert = self.create_dessert()
        dessert.prepare()
        dessert.serve()
        return dessert


# -------------------------------------
# Concrete Creators
# 
# Note: In this example, we are only creating 1 product - A dessert.
# -------------------------------------
class ConeMachine(DessertMachineFactory):
    def create_dessert(self) -> Dessert:
        return Cone()


class SundaeMachine(DessertMachineFactory):
    def create_dessert(self) -> Dessert:
        return Sundae()


class MilkshakeMachine(DessertMachineFactory):
    def create_dessert(self) -> Dessert:
        return Milkshake()