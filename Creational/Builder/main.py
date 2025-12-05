from builder import ConcreteHouseBuilder
from director import ConstructionDirector


if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = ConstructionDirector(builder)

    basic_house = director.build_basic_house()
    print("Basic House:", basic_house)

    luxury_builder = ConcreteHouseBuilder()
    luxury_director = ConstructionDirector(luxury_builder)
    
    luxury_house = luxury_director.build_luxury_house()
    print("Luxury House:", luxury_house)