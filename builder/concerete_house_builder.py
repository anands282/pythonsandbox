from house_builder import HouseBuilder
from house import House


class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_basement(self):
        self.house.basement = "cement"

    def build_walls(self):
        self.house.walls = "brick"

    def build_roof(self):
        self.house.roof = "tiles"

    def build_interior(self):
        self.house.interior = "self made"

    def get_house(self) -> House:
        return self.house
