from concerete_house_builder import ConcreteHouseBuilder
from director import Director

if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = Director(builder)
    director.construct_house()
    house = builder.get_house()
    print(house)
