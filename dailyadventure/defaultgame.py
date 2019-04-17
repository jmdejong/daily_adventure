
from .game import Game
from .dungeons.farm import Farm
from .dungeons.bed import Bed
from .dungeons.carpenter import Carpenter
from .dungeons.blacksmith import Blacksmith
from .dungeons.training import Training
from .dungeons.granary import Granary
from .dungeons.wood import Wood
from .dungeons.woodmarket import WoodMarket

def make_game():
    return Game([Farm(), Bed(), Carpenter(), Blacksmith(), Training(), Granary(), Wood(), WoodMarket()], default_dungeon="bed")
