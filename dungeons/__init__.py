
from availability import Availability

class Dungeon:
    
    name = None
    action = None
    description = None
    
    def get_action(self):
        return self.action
    
    def get_description(self):
        return self.description
    
    def get_availability(self, player):
        return Dungeon.hidden
    
    def can_see(self, player):
        return not self.get_availability(player).hidden
    
    def can_enter(self, player):
        return self.get_availability(player).available
    
    def entry_reason(self, player):
        return self.get_availability(player).reason
    
    def enter(self, player):
        pass
    
    
    available = Availability(True, True, None)
    hidden = Availability(False, False, None)
    @classmethod
    def unavailable(cls, reason):
        return Availability(True, False, reason)
