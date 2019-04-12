
from .game import Game
from .dungeons.farm import Farm
from .dungeons.bed import Bed
from .dungeons.carpenter import Carpenter
from .dungeons.blacksmith import Blacksmith
from .dungeons.training import Training
from .dungeons.granary import Granary

def make_game():
    return Game([Farm(), Bed(), Carpenter(), Blacksmith(), Training(), Granary()], default_dungeon="bed")
