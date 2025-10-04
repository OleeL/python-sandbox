from items.key import Key
from room import Room
from door import Door

rusty_key = Key("Rusty Key")
golden_key = Key("Golden Key")

ROOM_MAP = {
    "hall": {
        "name": "Hall",
        "north": "kitchen",
        "south": "bedroom",
        "east": "living_room",
        "west": "bathroom",
        "description": "A spacious hallway with high ceilings and large windows.",
        "items": [rusty_key, golden_key]
    },
    "kitchen": {
        "name": "Kitchen",
        "north": "dining_room",
        "south": "hall",
        "east": "pantry",
        "west": "garage",
        "lock": Door(key=rusty_key, description="A rusty lock"),
        "description": "A well-equipped kitchen with a large island and plenty of storage space.",
        "items": []
    },
    "bedroom": {
        "name": "Bedroom",
        "north": "hall",
        "south": "bathroom",
        "east": "closet",
        "lock": Door(key = golden_key, description="A golden lock"),
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
        "items": []
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

class GameMap:
    """
    This class takes a dictionary-based map (from dnd_map.py) and converts it to actual Room objects,
    hooking up references between rooms for north, south, east, and west.
    """
    def __init__(self, map_data):
        self.__map = map_data
        self.map = self.__to_room_dict()

    def __to_room(self, room_key):
        data = self.__map[room_key]
        room_door = data.get("lock")

        room_items = []
        for item_info in data.get("items", []):
            if isinstance(item_info, dict) and "secret" in item_info:
                room_items.append(Key(item_info["name"], item_info["secret"]))
            else:
                room_items.append(item_info)

        return Room(
            name=data["name"],
            description=data["description"],
            north=data["north"],
            south=data["south"],
            east=data["east"],
            west=data["west"],
            items=room_items,
            door=room_door
        )

    def __to_room_dict(self):
        """
        1st pass: create all Room objects (with placeholders for n/s/e/w).
        2nd pass: transform those n/s/e/w strings into room references.
        """
        obj = {}
        # First pass: create the rooms
        for key in self.__map.keys():
            obj[key] = self.__to_room(key)

        # Second pass: wire up the references
        for key, room_obj in obj.items():
            if room_obj.north in obj:
                room_obj.north = obj[room_obj.north]
            if room_obj.south in obj:
                room_obj.south = obj[room_obj.south]
            if room_obj.east in obj:
                room_obj.east = obj[room_obj.east]
            if room_obj.west in obj:
                room_obj.west = obj[room_obj.west]

        return obj

    def get_room(self, room_key):
        return self.map[room_key]

    def get_direction(self, room_key, direction):
        room = self.get_room(room_key)
        return self.get_room(getattr(room, direction))
