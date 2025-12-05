from builder import HouseBuilder

# -----------------------------
# Director
# -----------------------------
class ConstructionDirector:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def build_basic_house(self):
        """Defines a basic construction workflow."""
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_rooms()

        return self.builder.get_house()

    def build_luxury_house(self):
        """Workflow for a luxury house."""
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_rooms()

        self.builder.add_garage()
        self.builder.add_swimming_pool()

        return self.builder.get_house()