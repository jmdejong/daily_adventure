
import random

from . import Dungeon
from dailyadventure.items import items


class Training(Dungeon):
        
    name = "training"
    action = "Train to become a warrior"
    cost = 1
    description = "Train at the combat school to become a real warrior. Cost: {} coin per day".format(cost)
    
    
    
    def get_availability(self, player):
        if player.inv.has(items.warrior_diploma) and player.lvl >= 1:
            return Dungeon.hidden
        if not player.inv.has(items.wooden_sword):
            return Dungeon.unavailable("You need a wooden sword to train at the combat school")
        if not player.inv.has(item.coins, self.cost):
            return Dungeon.unavailable("You can't affort the combat school. You must pay {} coin{} per day".format(self.cost, "" if self.cost == 1 else "s"))
        if player.health < player.maxhealth:
            return Dungeon.unavailable("You need to be completely fit to train at the combat school. Give your wounds some rest")
        return Dungeon.available
    
    def enter(self, player):
        player.coins.remove(item.coins, self.cost)
        if player.lvl >= 1:
            player.inv.add(items.warrior_diploma)
            player.tell("You are already a warrior. After a brief exam the trainers agreed to give you a warrior diploma")
            return
        
        damage = max(random.normalvariate(15, 5), 0)
        
        player.health -= damage
        if player.health <= 0:
            player.health = 0
            player.coins.add(item.coins, self.cost)
            player.tell("You got completely knocked out in a training accident. You got your payment back though")
            return
        xp = random.uniform(0.2, 0.8)
        player.lvl = min(player.lvl + xp, 1)
        if player.lvl < 1:
            player.tell("You trained hard and learned a lot, but you weren't able to pass the warrior exam. Try again soon! Your effort is not lost!")
        else:
            player.inv.add(items.warrior_diploma)
            player.tell("You passed the warrior exam! Congratulations! You have received a warrior diploma")
            player.tell("Level up! You are now level 1")
