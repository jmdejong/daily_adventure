
import random

from . import Dungeon
from dailyadventure.items import items


class Carpentry(Dungeon):
    
    
    name = "carpentry"
    action = "Make a wooden sword"
    description = "Make a wooden sword out of sticks"
    cost = 5
    
    
    def get_availability(self, player):
        if not player.inv.has(items.stick, self.cost):
            return Dungeon.hidden
            
        if player.health < player.maxhealth:
            return Dungeon.unavailable("You need to be completely fit before crafting here. Give your wounds some rest")
        return Dungeon.available
    
    def enter(self, player):
        player.inv.remove(items.stick, self.cost)
        player.inv.add(items.wooden_sword)
        player.tell("You worked hard in the carpentry and built your own wooden sword!")
