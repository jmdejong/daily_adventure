



class Dungeon:
    
    name = None
    action = None
    description = None
    
    def get_action(self):
        return self.action
    
    def get_description(self):
        return self.description
    
    def cannot_enter(self, player):
        return True
    
    def enter(self, player):
        pass
    
    
