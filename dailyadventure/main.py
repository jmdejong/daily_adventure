#!/usr/bin/env python3

import os
import sys
import json
import re
from datetime import datetime, timezone
import logging
from argparse import ArgumentParser

from .utils import write_safe

from .input import Input

from .defaultgame import make_game

savefile = "save/save.json"

inputdir = "input/"
inputfilesuffix = ".input.txt"
inputfnames = inputdir + "{}.input.txt"
playername_extract = re.compile(inputdir + r'(\w+)' + inputfilesuffix)

playerdatafiles = "players/{}.json"
defaultdatafile = "defaultinfo.json"


def get_data_dir():
    return os.environ.get("DAILY_ADVENTURE_DATA", os.path.join(os.path.dirname(__file__), "..", "data"))

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
        logging.warning("could not get player name from file {}".format(fname))
        return None
    name = match.group(1)
    try:
        with open(fname, "r") as f:
            inp = f.read()
    except OSError as e:
        logging.warning("could not read input for player {} (file: {}): {}".format(name, fname, e))
        return None
    logging.info("input for player {}:\n{}".format(name, inp))
    lines = inp.splitlines()[:2]
    return Input(name, *lines)


def load_inputs():
    inputs = []
    try:
        inputfiles = [os.path.join(inputdir, fname) for fname in os.listdir(inputdir)]
    except OSError:
        logging.warning("unable to load player inputs")
        inputfiles = []
    for fname in inputfiles:
        data = load_player_input(fname)
        if data is not None:
            inputs.append(data)
    return inputs

NEW = "new"
UPDATE = "update"
REFRESH = "refresh"

def main():
    parser = ArgumentParser()
    parser.add_argument("action", choices=[NEW, UPDATE, REFRESH])
    parser.add_argument("--data-path")
    args = parser.parse_args()
    
    if args.data_path is not None:
        data_dir = args.data_path
    else:
        data_dir = get_data_dir()
    os.chdir(data_dir)
    
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        filename=os.path.join(
            "logs",
            datetime.utcnow().isoformat(timespec="seconds") + ".log"))
    logging.getLogger('').addHandler(logging.StreamHandler())
    
    logging.info("Daily Adventure update. UTC time: {datetime}".format(datetime=datetime.utcnow()))
    logging.info("creating game")
    game = make_game()
    
    
    if len(sys.argv) < 2 or args.action != NEW:
        logging.info("loading saved game data")
        try:
            savedata = load_save_data()
        except OSError:
            logging.error("Unable to open save. Make sure the savefile exist as {} or create a new save with `{} new`".format(savefile, sys.argv[0]))
            raise
        game.load(savedata)
    
    if args.action != REFRESH:
        logging.info("load player inputs")
        inputs = load_inputs()
        
        logging.info("update")
        game.day(inputs)
    
    logging.info("save game data")
    savedata = json.dumps(game.save())
    os.makedirs(os.path.dirname(savefile), exist_ok=True)
    write_safe(savefile, savedata, mode=0o600)
    
    logging.info("inform players")
    for playername in game.players:
        infofile = playerdatafiles.format(playername)
        data = json.dumps(game.get_visible_data(playername))
        os.makedirs(os.path.dirname(infofile), exist_ok=True)
        write_safe(infofile, data, mode=0o600)
    
    default_info = json.dumps(game.get_visible_data(None))
    write_safe(defaultdatafile, default_info)
    
    
    if args.action != REFRESH:
        logging.info("clear input")
        try:
            os.makedirs(inputdir, exist_ok=True)
            inputfiles = os.listdir(inputdir)
        except OSError:
            inputfiles = []
        for fname in inputfiles:
            os.remove(os.path.join(inputdir, fname))
    
    logging.info("done")
    print("updated successfully")

