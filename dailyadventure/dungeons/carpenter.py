
import random

from . import Dungeon
from dailyadventure.items import items


class Carpenter(Dungeon):
    
    
    name = "carpenter"
    action = "Work for carpenter"
    description = "Help the carpenter out in the workshop. {} will reward you with a wooden training sword.".format(random.choice(["He", "She", "They"]))
    
    
    
    def get_availability(self, player):
        if player.inv.has(items.wooden_sword):
            return Dungeon.hidden
            
        if player.health < player.maxhealth:
            return Dungeon.unavailable("You need to be completely fit to work for the carpenter. Give your wounds some rest")
        return Dungeon.available
    
    def enter(self, player):
        player.inv.add(items.wooden_sword)
        player.tell("You worked for the carpenter and were rewarded a wooden training sword")
