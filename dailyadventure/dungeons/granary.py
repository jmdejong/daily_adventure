
import random

from . import Dungeon
from dailyadventure.items import items

_wage = 30

class Granary(Dungeon):
        
    name = "granary"
    action = "Fight rats"
    wage = _wage
    description = "The farmer will pay reward you {} coins if you kill the rats infesting the granary of {} farm".format(_wage, random.choice(["his", "her", "their"]))
    
    
    
    def get_availability(self, player):
        if not player.inv.has(items.dagger):
            return Dungeon.hidden
        if player.health < player.maxhealth:
            return Dungeon.unavailable("You need to be completely fit to fight rats. Give your wounds some rest")
        return Dungeon.available
    
    def enter(self, player):
        damage = max(random.normalvariate(15, 5), 0)
        player.health -= damage
        if player.health <= 0:
            player.tell("You failed to defeat the rats; the rats defeated you! You don't get the reward. The farmer pities you and still gives you some coins")
            player.inv.add(items.coins, 2)
        else:
            player.inv.add(items.coins, self.wage)
            player.tell("You defeated the rats! The farmer gives you the reward of {} coins.".format(self.wage))
