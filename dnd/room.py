class Room:
    def __init__(self, name, description, north, south, east, west, items, door=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.door = door   # optional Door object

    def __str__(self):
        return f"{self.name}: {self.description}"
