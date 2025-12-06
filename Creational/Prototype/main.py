from loadout_prototype import Loadout

class LoadoutManager:
    """Stores prototype loadouts players can clone."""
    def __init__(self):
        self.prototypes = {}

    def register(self, key: str, prototype: Loadout):
        self.prototypes[key] = prototype

    def clone(self, key: str) -> Loadout:
        prototype = self.prototypes.get(key)

        if not prototype:
            raise ValueError(f"No prototype found for '{key}'")
        return prototype.clone()


if __name__ == "__main__":
    manager = LoadoutManager()

    # Create a base prototype loadout
    assasin_loadout = Loadout(
        name="Assassin",
        weapon="Silenced Dagger",
        armor="Shadow Cloak",
        abilities=["Invisibility", "Backstab", "Silent Step"]
    )

    # Register it so the player can clone it anytime
    manager.register("assasin", assasin_loadout)

    # Clone original loadout
    stealth_assasin_loadout = manager.clone("assasin")

    # Modify new loadout
    stealth_assasin_loadout.name = "Stealth Assassin"
    stealth_assasin_loadout.weapon = "Silent Crossbow"
    stealth_assasin_loadout.abilities.append("Poison Bolt")

    print(F"This is the assasin loadout: ", assasin_loadout, "\n")
    print(f"This is the stealth assasin loadout: ", stealth_assasin_loadout)