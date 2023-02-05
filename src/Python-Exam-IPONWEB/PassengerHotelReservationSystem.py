class Passenger:
    def __init__(self, name, city):
        self.__name = name
        self.__city = city
        self.__rooms = {}

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def rooms(self):
        return self.__rooms

    def __repr__(self):
        return f"Passenger's name is {self.name}, he/she flies to {self.city}, rooms are {self.rooms}."


class Hotel:
    def __init__(self, city, rooms):
        self.__city = city
        if type(rooms) != dict:
            raise HotelError("Invalid rooms for hotel.")
        if len(rooms.keys()) != 3:
            raise HotelError("Rooms have 3 types.")
        for key in rooms.keys():
            if key not in ['penthouse', 'single', 'double']:
                raise HotelError("Invalid rooms for the hotel.")
            if type(rooms[key]) != int or rooms[key] < 0:
                raise HotelError("Invalid rooms for the hotel.")
        self.rooms = rooms

    @property
    def city(self):
        return self.__city

    def __repr__(self):
        return f"The hotel is in {self.city} city, it has {self.rooms} rooms."

    def free_rooms_list(self, room):
        return self.rooms[room]

    def reserve_rooms(self, room, count):
        if count > self.rooms[room]:
            raise BookingError("There are not that much at that room type.")
        self.rooms[room] -= count


def book(passenger, hotel, room, count):
    if type(passenger) != Passenger or type(hotel) != Hotel or room not in ['penthouse', 'single', 'double'] or type(
            count) != int or count <= 0 or passenger.city != hotel.city:
        raise BookingError("Invalid booking data")
    hotel.reserve_rooms(room, count)
    try:
        passenger.rooms[room] += count
    except:
        passenger.rooms[room] = count


class HotelError(Exception):
    pass


class BookingError(Exception):
    pass


p1 = Passenger('Ani', "Frankfurt")
p2 = Passenger('Hrach', "Warsaw")
p3 = Passenger("Nellita", "Seoul")
p4 = Passenger("Kim", "Seoul")
p5 = Passenger("Hasmik", "Frankfurt")
p6 = Passenger("Ara", "Frankfurt")

h1 = Hotel("Frankfurt", {'single': 15, 'double': 1, 'penthouse': 0})
h2 = Hotel("Seoul", {'single': 24, 'double': 5, 'penthouse': 1})
h3 = Hotel("Warsaw", {'single': 13, 'double': 3, 'penthouse': 0})

book(p1, h1, 'double', 1)
print(p1)
print(h1)
print()
book(p2, h3, 'single', 10)
print(p2)
print(h3)
print()
book(p3, h2, 'double', 3)
print(p3)
print(h2)
print(h1.free_rooms_list('double'))
