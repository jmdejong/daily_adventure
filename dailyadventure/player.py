
from .inventory import Inventory
from .items import items

class Player:
    
    def __init__(self, name):
        
        self.name = name
        
        self.lvl = 0
        self.inv = Inventory()
        self.maxhealth = 100
        self.health = self.maxhealth
        self.coins = 0
        self.messages = []
        
    
    def morning(self, actions):
        pass
    
    def explore(self, dungeon):
        dungeon.enter(self)
        
    def can_enter(self, dungeon):
        return dungeon.can_enter(self)
    
    def can_see(self, dungeon):
        return dungeon.can_see(self)
    
    def tell(self, message):
        self.messages.append(message)
    
    def get_messages(self):
        return self.messages
    
    def view(self, game):
        return {
            "options": game.get_options(self),
            "messages": self.get_messages(),
            "health": int(self.health),
            "maxhealth": self.maxhealth,
            "lvl": int(self.lvl),
            "default": game.default_dungeon.name,
            "inventory": self.inv.view()
        }
    
    def save(self):
        return {
            "name": self.name,
            "lvl": self.lvl,
            "inv": self.inv.save(),
            "health": self.health,
            "maxhealth": self.maxhealth
        }
    
    @classmethod
    def load(cls, data):
        p = Player(data["name"])
        p.inv = Inventory(data["inv"])
        p.lvl = data["lvl"]
        p.maxhealth = data["maxhealth"]
        p.health = data["health"]
        if "coins" in data and not p.inv.has(items.coins):
            p.inv.add(items.coins, data["coins"])
        return p
