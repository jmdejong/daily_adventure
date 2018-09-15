#!/usr/bin/python3


from game import Game
from dungeons.farm import Farm
from dungeons.bed import Bed
from input import Input

def main():
    
    
    game = Game([Farm(), Bed()], default_dungeon="Bed")
    
    inputs = [
        Input({
            "player": "troido",
            "morning": [],
            "dungeon": "Farm"})]
    
    game.day({inp.player: inp for inp in inputs})
    
    print(game.save())
    
    game.players["troido"].health = 25
    
    game.day({})
    
    print(game.save())
    print(game.get_options("troido"))



if __name__ == "__main__":
    main()
