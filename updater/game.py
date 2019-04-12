

from .player import Player


class Game:
    
    def __init__(self, dungeons=[], buildings=[], default_dungeon=None):
        self.players = {}
        self.dungeons = {dungeon.name: dungeon for dungeon in dungeons}
        self.buildings = {building.name for building in buildings}
        self.default_dungeon = self.dungeons.get(default_dungeon)
        
    def load(self, data):
        self.players = {pd["name"]: Player.load(pd) for pd in data["players"]}
    
    def save(self):
        return {
            "players": [player.save() for player in self.players.values()]
            }
    
    
    def day(self, inputlist):
        inputs = {inp.player: inp for inp in inputlist}
        self.morning(inputs)
        self.afternoon(inputs)
    
    def morning(self, inputs):
        for name, inp in inputs.items():
            player = self.players.get(name)
            if player is None:
                player = Player(name)
                self.players[name] = player
            
            # TODO morning action
    
    def afternoon(self, inputs):
        for name, player in self.players.items():
            inp = inputs.get(name)
            if inp:
                dungeon = self.dungeons.get(inp.dungeon)
            else:
                dungeon = None
            if not dungeon or not player.can_enter(dungeon):
                if self.default_dungeon and player.can_enter(self.default_dungeon):
                    dungeon = self.default_dungeon
                else:
                    continue
            player.explore(dungeon)
            
    def get_options(self, player):
        return {
            dungeon.name: {
                    "action": dungeon.get_action(),
                    "description": dungeon.get_description(),
                    "available": player.can_enter(dungeon),
                    "reason": dungeon.entry_reason(player),
                    "difficulty": dungeon.get_difficulty()}
                for dungeon in self.dungeons.values()
                if player.can_see(dungeon)}
    
    def get_visible_data(self, playername):
        if playername in self.players:
            player = self.players[playername]
        else:
            player = Player(playername)
        return {
            "options": self.get_options(player),
            "messages": player.get_messages(),
            "health": int(player.health),
            "maxhealth": player.maxhealth,
            "coins": player.coins,
            "lvl": int(player.lvl),
            "default": self.default_dungeon.name,
            "inventory": player.inv}
    
    def tell_player(playername, message):
        if playername not in self.players:
            return False
        self.player[playername].tell(message)
        return True



