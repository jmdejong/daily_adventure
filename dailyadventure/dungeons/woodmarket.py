
import random

from .dungeon import Dungeon
from ..items import items

class WoodMarket(Dungeon):
    
    name = "firewood"
    action = "Sell your firewood on the market"
    inv_price = 3
    description = "Sell the firewood you collected on the market. You get one coin for {} firewood".format(inv_price)
    
    
    def get_availability(self, player):
        if player.inv.has(items.firewood, inv_price):
            return Dungeon.available
        else:
            return Dungeon.hidden
    
    
    def enter(self, player):
        sales = min(random.randrange(20, 80), player.inv.get(items.firewood) // inv_price)
        player.inv.remove(items.firewood, sales * inv_price)
        player.inv.add(items.coins, sales)
        player.tell("You sold {} firewood for {} coins in total.".format(sales * inv_price, sales))
