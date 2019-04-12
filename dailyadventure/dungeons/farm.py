
import random

from . import Dungeon



class Farm(Dungeon):
    
    
    name = "farm"
    action = "Work on farm"
    wage = 5
    description = "The farmer will pay you {} coins if you work a day on {} farm".format(wage, random.choice(["his", "her", "their"]))
    
    
    
    def get_availability(self, player):
        if player.health < player.maxhealth:
            return Dungeon.unavailable("You need to be completely fit to work on the farm. Give your wounds some rest")
        return Dungeon.available
    
    def enter(self, player):
        player.coins += self.wage
        player.tell("You worked on the farm and made {} coins. You now have {} coins".format(self.wage, player.coins))
