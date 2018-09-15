

class Player():
    
    def __init__(self, name):
        
        self.name = name
        
        self.lvl = 0
        self.inv = []
        self.health = 0
        self.maxhealth = 100
        self.coins = 0
        
    
    def morning(self, actions):
        pass
    
    def explore(self, dungeon):
        dungeon.enter(self)
        
    def can_enter(self, dungeon):
        return dungeon.cannot_enter(self) is False
    
    def can_see(self, dungeon):
        not (dungeon.cannot_enter(self) is True)
    
    def save(self):
        return {
            "name": self.name,
            "lvl": self.lvl,
            "inv": self.inv,
            "health": self.health,
            "maxhealth": self.maxhealth,
            "coins": self.coins}
    
