
import random

from .dungeon import Dungeon
from ..items import items

class Wood(Dungeon):
    
    name = "wood"
    action = "Gather wood in the forest"
    description = "Collect sticks and firewood in the forest. The sticks can be used to craft things and the firewood can be sold for money."
    
    
    def get_availability(self, player):
        return Dungeon.available
    
    
    def enter(self, player):
        firewood = random.randrange(5, 25)
        sticks = random.randrange(2, 6)
        player.inv.add(items.firewood, firewood)
        player.inv.add(items.stick, sticks)
        player.tell("You collected {} sticks and {} firewood.".format(sticks, firewood))
