

class Player():
    
    def __init__(self, name):
        
        self.name = name
        
        self.lvl = 0
        self.inv = []
        self.maxhealth = 100
        self.health = self.maxhealth
        self.coins = 0
        
    
    def morning(self, actions):
        pass
    
    def explore(self, dungeon):
        dungeon.enter(self)
        
    def can_enter(self, dungeon):
        return dungeon.can_enter(self)
    
    def can_see(self, dungeon):
        return dungeon.can_see(self)
    
    def save(self):
        return {
            "name": self.name,
            "lvl": self.lvl,
            "inv": self.inv,
            "health": self.health,
            "maxhealth": self.maxhealth,
            "coins": self.coins}
    
