from items.key import Key

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.health = 100

    def move(self, direction):
        # Determine room to move to
        if direction == "north":
            next_room = self.location.north
        elif direction == "south":
            next_room = self.location.south
        elif direction == "east":
            next_room = self.location.east
        elif direction == "west":
            next_room = self.location.west
        else:
            print("Invalid direction.")
            return

        if not next_room:
            print("You can't go that way.")
            return

        if next_room.door and next_room.door.is_locked:
            print(f"The door to the {next_room.name} is locked. Trying your keys...")
            if not self.__try_unlock(next_room.door):
                print("You don't have the right key.")
                return
            else:
                print(f"You unlocked the door to the {next_room.name}!")

        self.location = next_room

    def __try_unlock(self, door):
        for item in self.inventory:
            if isinstance(item, Key) and door.use_key(item):
                return True
        return False

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"You picked up: {item}")
