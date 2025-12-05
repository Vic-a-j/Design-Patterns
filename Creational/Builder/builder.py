from abc import ABC, abstractmethod

# -----------------------------
# Product
# -----------------------------
class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None
        self.rooms = 0
        self.has_garage = False
        self.has_swimming_pool = False

    def __repr__(self):
        return (
            f"House(foundation={self.foundation}, "
            f"structure={self.structure}, roof={self.roof}, "
            f"rooms={self.rooms}, garage={self.has_garage}, "
            f"pool={self.has_swimming_pool})"
        )


# -----------------------------
# Abstract Builder
# -----------------------------
class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def build_foundation(self):
        ...

    @abstractmethod
    def build_structure(self):
        ...

    @abstractmethod
    def build_roof(self):
        ...

    @abstractmethod
    def build_rooms(self):
        ...

    def add_garage(self):
        self.house.has_garage = True

    def add_swimming_pool(self):
        self.house.has_swimming_pool = True

    def get_house(self):
        return self.house


# -----------------------------
# Concrete Builder
# -----------------------------
class ConcreteHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Concrete, rebar, and gravel"

    def build_structure(self):
        self.house.structure = "Wood and brick"

    def build_roof(self):
        self.house.roof = "Concrete roof tiles"

    def build_rooms(self):
        self.house.rooms = 4