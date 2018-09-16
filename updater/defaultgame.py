
from game import Game
from dungeons.farm import Farm
from dungeons.bed import Bed

def make_game():
    return Game([Farm(), Bed()], default_dungeon="Bed")
