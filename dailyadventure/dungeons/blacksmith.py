

from . import Dungeon
from dailyadventure.items import items

class Blacksmith(Dungeon):
    
    
    name = "blacksmith"
    action = "Buy dagger"
    cost = 10
    description = "Buy a dagger from the blacksmith for {} coins".format(cost)
    
    
    
    def get_availability(self, player):
        if player.inv.has(items.dagger) or not player.inv.has(items.warrior_diploma):
            return Dungeon.hidden
        if !player.inv.has(items.coins, self.cost):
            return Dungeon.unavailable("You don't have enough money to buy a dagger. You need {} coins".format(self.cost))
        return Dungeon.available
    
    def enter(self, player):
        player.inv.add("dagger")
        player.inv.remove(items.coins, self.cost)
        player.tell("You bought a dagger for from the blacksmith for {} coins. You spent the rest of the day practicing with your new weapon".format(self.cost))
