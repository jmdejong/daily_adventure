#!/usr/bin/env python3

import pytest

from game import Game
from dungeons.farm import Farm
from dungeons.bed import Bed
from input import Input

def test_game():
    
    
    game = Game([Farm(), Bed()], default_dungeon="bed")
    
    
    
    inp = Input("troido", "", "farm")
    inputs = [inp]
    
    
    game.day(inputs)
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["name"] == "troido"
    assert players[0]["health"] == 100
    assert players[0]["coins"] == Farm.wage
    options = game.get_visible_data("troido")["options"]
    assert "farm" in options
    assert options["farm"]["available"]
    assert "bed" in options
    assert options["bed"]["available"]
    
    
    game.players["troido"].health = 25
    
    options = game.get_visible_data("troido")["options"]
    assert "farm" in options
    assert not options["farm"]["available"]
    assert "bed" in options
    assert options["bed"]["available"]
    
    
    game.day([])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 75
    assert players[0]["coins"] == Farm.wage
    options = game.get_visible_data("troido")["options"]
    assert "farm" in options
    assert not options["farm"]["available"]
    assert "bed" in options
    assert options["bed"]["available"]
    
    
    game.day([inp])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 100
    assert players[0]["coins"] == Farm.wage
    options = game.get_visible_data("troido")["options"]
    assert "farm" in options
    assert options["farm"]["available"]
    assert "bed" in options
    assert options["bed"]["available"]
    
    
    inp.dungeon = "bed"
    game.day([inp])
    
    save = game.save()
    assert "players" in save
    players = save["players"]
    assert len(players) == 1
    assert players[0]["health"] == 100
    assert players[0]["coins"] == Farm.wage
    options = game.get_visible_data("troido")["options"]
    assert "farm" in options
    assert options["farm"]["available"]
    assert "bed" in options
    assert options["bed"]["available"]
    
    print("done")
    
    



if __name__ == '__main__':
    pytest.main(['-v', '-x', '-s'])
