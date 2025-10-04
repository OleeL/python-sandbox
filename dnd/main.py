from game_map import GameMap, ROOM_MAP
from player import Player
from game import Game

if __name__ == "__main__":
    map_obj = GameMap(ROOM_MAP)
    player = Player("Player", map_obj.get_room("hall"))
    game = Game(player, map_obj)
    game.start()
