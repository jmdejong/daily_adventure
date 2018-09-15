

import json

class Input:
    
    
    def __init__(self, data, player=None):
        self.player = player or  data.get("player")
        self.morning_actions = data["morning"]
        self.dungeon = data["dungeon"]
    
