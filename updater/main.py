#!/usr/bin/python3

import os
import sys
import json
import re

try:
    from defaultgame import make_game
except ImportError:
    thisdir = os.path.dirname(__file__)
    sys.path = [thisdir] + sys.path
    from defaultgame import make_game

from utils import write_safe

from input import Input

savefile = "save/save.json"

inputdir = "input/"
inputfilesuffix = ".input.txt"
inputfnames = inputdir + "{}.input.txt"
playername_extract = re.compile(inputdir + r'(\w+)' + inputfilesuffix)

playerdatafiles = "players/{}.json"


def get_data_dir():
    if len(sys.argv) > 1 and sys.argv[-1] != "new":
        return sys.argv[-1]
    return os.environ.get("DAILY_ADVENTURE_DATA", "../data/")

def load_save_data():
    with open(savefile, "r") as f:
        savedata = json.load(f)
    return savedata

def tell_player(player, text):
    pass

def load_player_input(fname):
    if not fname.endswith(inputfilesuffix):
        return None
    match = playername_extract.match(fname)
    if not match:
        return None
    name = match.group(1)
    try:
        with open(fname, "r") as f:
            inp = f.read()
    except OSError:
        return None
    lines = inp.splitlines()[:2]
    return Input(name, *lines)


def load_inputs():
    inputs = []
    try:
        inputfiles = [os.path.join(inputdir, fname) for fname in os.listdir(inputdir)]
    except OSError:
        inputfiles = []
    for fname in inputfiles:
        data = load_player_input(fname)
        if data is not None:
            inputs.append(data)
    return inputs

def main():
    
    print("")
    print("creating game")
    game = make_game()
    
    os.chdir(get_data_dir())
    
    if len(sys.argv) < 2 or sys.argv[1] != "new":
        print("loading saved game data")
        try:
            savedata = load_save_data()
        except OSError:
            print("Unable to open save. Make sure the savefile exist as {} or create a new save with `{} new`".format(savefile, sys.argv[0]), file=sys.stderr)
            return
        game.load(savedata)
    
    print("load player inputs")
    inputs = load_inputs()
    
    print("update")
    game.day(inputs)
    
    print("save game data")
    savedata = json.dumps(game.save())
    os.makedirs(os.path.dirname(savefile), exist_ok=True)
    write_safe(savefile, savedata)
    
    print("inform players")
    for playername in game.players:
        infofile = playerdatafiles.format(playername)
        data = json.dumps(game.get_visible_data(playername))
        os.makedirs(os.path.dirname(infofile), exist_ok=True)
        write_safe(infofile, data)
    
    print("clear input")
    try:
        os.makedirs(inputdir, exist_ok=True)
        inputfiles = os.listdir(inputdir)
    except OSError:
        inputfiles = []
    for fname in inputfiles:
        os.remove(os.path.join(inputdir, fname))
    
    print("done")
    print("")
    
    



if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    main()
