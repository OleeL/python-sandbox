class GameMap:
    __map = {
        "hall": {
            "name": "Hall",
            "north": "kitchen",
            "south": "bedroom",
            "east": "living_room",
            "west": "bathroom",
            "description": "A spacious hallway with high ceilings and large windows.",
            "items": []
        },
        "kitchen": {
            "name": "Kitchen",
            "north": "hall",
            "south": "dining_room",
            "east": "pantry",
            "west": "garage",
            "description": "A well-equipped kitchen with a large island and plenty of storage space.",
            "items": []
        },
        "bedroom": {
            "name": "Bedroom",
            "north": "hall",
            "south": "bathroom",
            "east": "closet",
            "west": "office",
            "description": "A cozy bedroom with a comfortable bed and a small desk.",
            "items": []
        },
        "living_room": {
            "name": "Living Room",
            "north": "hall",
            "south": "dining_room",
            "east": "balcony",
            "west": "pantry",
            "description": "A comfortable living room with a large sofa and a coffee table.",
            "items": []
        },
        "bathroom": {
            "name": "Bathroom",
            "north": "bedroom",
            "south": "hall",
            "east": "pantry",
            "west": "garage",
            "description": "A modern bathroom with a large shower and a bathtub.",
            "items": []
        },
        "dining_room": {
            "name": "Dining Room",
            "north": "kitchen",
            "south": "living_room",
            "east": "pantry",
            "west": "garage",
            "description": "A spacious dining room with a large table and comfortable chairs.",
            "items": ["key"]
        },
        "pantry": {
            "name": "Pantry",
            "north": "kitchen",
            "south": "living_room",
            "east": "balcony",
            "west": "bathroom",
            "description": "A well-stocked pantry with a variety of snacks and drinks.",
            "items": ["snacks", "drinks"]
        },
        "garage": {
            "name": "Garage",
            "north": "bathroom",
            "south": "dining_room",
            "east": "pantry",
            "west": "office",
            "description": "A spacious garage with a workshop and storage space.",
            "items": []
        },
        "closet": {
            "name": "Closet",
            "north": "bedroom",
            "south": "office",
            "east": "balcony",
            "west": "pantry",
            "description": "A spacious closet with a variety of clothes and accessories.",
            "items": ["clothes", "accessories"]
        },
        "office": {
            "name": "Office",
            "north": "bedroom",
            "south": "garage",
            "east": "balcony",
            "west": "closet",
            "description": "A spacious office with a desk and comfortable chair.",
            "items": ["chair", "desk"]
        },
        "balcony": {
            "name": "Balcony",
            "north": "living_room",
            "south": "pantry",
            "east": "office",
            "west": "closet",
            "description": "A spacious balcony with a view of the city.",
            "items": []
        }
    }

    def __init__(self):
        self.map = self.__to_room_dict()

    def __to_room(self, room_key):
        return Room(
            self.__map[room_key]["name"],
            self.__map[room_key]["description"],
            self.__map[room_key]["north"],
            self.__map[room_key]["south"],
            self.__map[room_key]["east"],
            self.__map[room_key]["west"],
            self.__map[room_key]["items"]
        )

    def __to_room_dict(self):
        obj = {}
        for key in self.__map.keys():
            obj[key] = self.__to_room(key)
        for key in self.__map.keys():
            obj[key].north = obj[obj[key].north]
            obj[key].south = obj[obj[key].south]
            obj[key].east = obj[obj[key].east]
            obj[key].west = obj[obj[key].west]

        return obj

    def get_room(self, room_key):
        return self.map[room_key]

class Game:
    def __init__(self, player, map):
        self.player = player
        self.map = map

    def start(self):
        print(self.player.location)
        while True:
            command = input("\nWhat do you want to do? ").lower()
            if command == "quit":
                break
            elif command == "look":
                print(self.player.location)
            elif command.startswith("go"):
                direction = command.split()[1]
                if direction not in ["north", "south", "east", "west"]:
                    print("Invalid direction.")
                else:
                    self.player.move(direction)
                    print(self.player.location)
            elif command == "help":
                print("Available commands:")
                print("quit - Quit the game")
                print("look - Look around")
                print("go <direction> - Move in a direction")
                print("help - Display this help message")
            else:
                print("I don't understand that command.")

class Room:
    def __init__(self, name, description, north, south, east, west, items):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items

    def __str__(self):
        return f"{self.name}: {self.description}"


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.health = 100

    def move(self, direction):
        if direction == "north":
            if self.location.north:
                self.location = self.location.north
            else:
                print("You can't go that way.")
        elif direction == "south":
            if self.location.south:
                self.location = self.location.south
            else:
                print("You can't go that way.")
        elif direction == "east":
            if self.location.east:
                self.location = self.location.east
            else:
                print("You can't go that way.")
        elif direction == "west":
            if self.location.west:
                self.location = self.location.west
            else:
                print("You can't go that way.")
        else:
            print("Invalid direction.")

map = GameMap()
player = Player("Player", map.get_room("hall"))
game = Game(player, map)
game.start()
