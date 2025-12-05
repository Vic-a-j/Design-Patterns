from abc import ABC, abstractmethod

# -------------------------------------
# Product Interface
# -------------------------------------
class Dessert(ABC):
    @abstractmethod
    def prepare(self) -> None:
        ...

    @abstractmethod
    def serve(self) -> None:
        ...


# -------------------------------------
# Concrete Products
# -------------------------------------
class Cone(Dessert):
    def prepare(self):
        print("Scooping ice cream onto a cone...")

    def serve(self):
        print("Serving a classic ice cream cone!\n")


class Sundae(Dessert):
    def prepare(self):
        print("Preparing bowl, adding ice cream scoops, pouring syrup...")

    def serve(self):
        print("Serving a delicious ice cream sundae!\n")


class Milkshake(Dessert):
    def prepare(self):
        print("Blending ice cream with milk and flavoring...")

    def serve(self):
        print("Serving a thick and creamy milkshake!\n")