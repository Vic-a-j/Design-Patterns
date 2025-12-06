from __future__ import annotations
import copy


# --- Prototype Interface ---
class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Loadout(Prototype):
    def __init__(self, name: str, weapon: str, armor: str, abilities: list):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.abilities = abilities

    def __str__(self):
        return (
            f"Loadout: {self.name}\n"
            f"  Weapon: {self.weapon}\n"
            f"  Armor: {self.armor}\n"
            f"  Abilities: {', '.join(self.abilities)}"
        )