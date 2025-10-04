class Player:
    def __init__(self, name, location: str | int = "hallway"):
        self.name = name
        self.inventory = []

steve = Player("Steve", 235235)
print(steve)
