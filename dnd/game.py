import sys
class Game:
    def __init__(self, player, map_obj):
        self.player = player
        self.map = map_obj

    def look(self):
        print(self.player.location)
        if self.player.location.items:
            print("You see:")
            for i, itm in enumerate(self.player.location.items):
                print(f" {i+1}. {itm}")

    def take(self, command):
        parts = command.split()
        if len(parts) < 2:
            print("Take what?")
            return
        target_item = " ".join(parts[1:])
        found = False
        items_taken = []
        for itm in self.player.location.items:
            item_name = itm if isinstance(itm, str) else itm.get_name()
            if target_item.lower() in item_name.lower():
                found = True
                items_taken.append(itm)
                self.player.pick_up_item(itm)
        for itm in items_taken:
            self.player.location.items.remove(itm)
        if not found:
            print("There is no such item here.")

    def go(self, direction):
        self.player.move(direction)
        print(self.player.location)

    def print_inventory(self):
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            print("You are carrying:")
            for itm in self.player.inventory:
                print(f"  - {itm}")

    def quit(self):
        print("Goodbye!")
        sys.exit(0)

    def print_help(self):
        print("\"Available\" commands:")
        print("quit - Quit the game")
        print("look - Look around")
        print("go <direction> - Move in a direction (north, south, east, west)")
        print("take <item name> - Pick up an item")
        print("inventory - Check your items")
        print("help - Display this help message")

    def start(self):
        print(self.player.location)
        while True:
            try:
                command = input("\nWhat do you want to do? ").lower().strip()
            except KeyboardInterrupt:
                print()
                self.quit()
            if command == "quit":
                self.quit()
            elif command == "look":
                self.look()
            elif command.startswith("go "):
                self.go(command.split(" ")[1])
            elif command.startswith("take "):
                self.take(command)
            elif command == "inventory":
                self.print_inventory()
            elif command == "help":
                self.print_help()
            else:
                print("I don't understand that command.")
