#!/usr/bin/python3


from game import Game
from dungeons.farm import Farm
from dungeons.bed import Bed
from input import Input

def main():
    
    
    game = Game([Farm(), Bed()], default_dungeon="Bed")
    
    print(game.save())
    
    
    inp = Input({
        "player": "troido",
        "morning": [],
        "dungeon": "Farm"})
    inputs = [inp]
    
    
    game.day(inputs)
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["name"] == "troido"
    assert players[0]["health"] == 100
    assert players[0]["coins"] == 10
    options = game.get_options("troido")
    assert "Farm" in options
    assert options["Farm"]["available"]
    assert "Bed" in options
    assert options["Bed"]["available"]
    
    
    game.players["troido"].health = 25
    
    options = game.get_options("troido")
    assert "Farm" in options
    assert not options["Farm"]["available"]
    assert "Bed" in options
    assert options["Bed"]["available"]
    
    
    game.day([])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 75
    assert players[0]["coins"] == 10
    options = game.get_options("troido")
    assert "Farm" in options
    assert not options["Farm"]["available"]
    assert "Bed" in options
    assert options["Bed"]["available"]
    
    
    game.day([inp])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 100
    assert players[0]["coins"] == 10
    options = game.get_options("troido")
    assert "Farm" in options
    assert options["Farm"]["available"]
    assert "Bed" in options
    assert options["Bed"]["available"]
    
    
    inp.dungeon = "Bed"
    game.day([inp])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 100
    assert players[0]["coins"] == 10
    options = game.get_options("troido")
    assert "Farm" in options
    assert options["Farm"]["available"]
    assert "Bed" in options
    assert options["Bed"]["available"]
    



if __name__ == "__main__":
    main()
