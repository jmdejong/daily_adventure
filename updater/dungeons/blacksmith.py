

from . import Dungeon

class Blacksmith(Dungeon):
    
    
    name = "blacksmith"
    action = "Work for carpenter"
    cost = 10
    description = "Buy a dagger from the blacksmith for {} coins".format(cost)
    
    
    
    def get_availability(self, player):
        if "dagger" in player.inv or not "warrior diploma" in player.inv:
            return Dungeon.hidden
        if player.coins < 1:
            return Dungeon.unavailable("You don't have enough money to buy a dagger. You need {} coins".format(self.cost))
        return Dungeon.available
    
    def enter(self, player):
        player.inv.append("dagger")
        player.coins -= self.cost
        player.tell("You bought a dagger for from the blacksmith for {} coins. You spent the rest of the day practicing with your new weapon".format(self.cost))
