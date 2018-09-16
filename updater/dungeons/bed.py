

from . import Dungeon


class Bed(Dungeon):
    
    
    name = "Bed"
    action = "Rest for the day"
    healing = 50
    description = "Rest a day to restore health. You will heal by 50 health points"
    
    
    
    def get_availability(self, player):
        return Dungeon.available
    
    def enter(self, player):
        oldhealth = player.health
        player.health = max(player.health, min(player.health + self.healing, player.maxhealth))
        healed = player.health - oldhealth
        player.tell("You rested this day and healed for {} health. Your current health is {}/{}".format(healed, player.health, player.maxhealth))
