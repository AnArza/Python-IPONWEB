class House:
    def __init__(self, building_type='Apartment', doors=0, windows=0, wall_material='brick'):
        self.building_type = building_type
        self.doors = doors
        self.windows = windows
        self.wall_material = wall_material

    def __repr__(self):
        return f"This is a {self.wall_material} {self.building_type} with {self.doors} door(s) and {self.windows} " \
               f"window(s)."


class HouseBuilder:
    def __init__(self):
        self.__house = House()

    def set_building_type(self, building_type):
        self.__house.building_type = building_type
        return self

    def set_doors(self, d):
        self.__house.doors = d
        return self

    def set_windows(self, w):
        self.__house.windows = w
        return self

    def set_wall_material(self, wm):
        self.__house.wall_material = wm
        return self

    def get_house(self):
        return self.__house


class HouseBoatDirector:
    @staticmethod
    def build():
        return HouseBuilder().set_building_type('House Boat').set_wall_material('Wood').set_doors(6).set_windows(
            8).get_house()


class CastleDirector:
    @staticmethod
    def build():
        return HouseBuilder().set_building_type('Castle').set_wall_material('Sandstone').set_doors(100).set_windows(
            200).get_house()


class IglooDirector:
    @staticmethod
    def build():
        return HouseBuilder().set_building_type('Igloo').set_wall_material('Ice').set_doors(1).get_house()


igloo = IglooDirector().build()
print(igloo)

castle = CastleDirector().build()
print(castle)

house_boat = HouseBoatDirector().build()
print(house_boat)
