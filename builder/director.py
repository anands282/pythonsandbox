from house_builder import HouseBuilder


class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_basement()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_interior()