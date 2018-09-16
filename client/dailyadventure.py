#!/usr/bin/python3

import sys
import os
import json
#import argparse

_dir = os.path.dirname(__file__)
if _dir:
    os.chdir(_dir)


commandname = sys.argv[1]

welcometext = """
Welcome to Daily Adventure
You can set one action for the day. This will be executed at UTC midnight.
You will then have to set a new command for the next day.
Run `{command} help` for instructions""".format(command=commandname)

helptext = """
Run `{command} report` or `{command}` for a full information listing.
Run `{command} do <input>` to pick an action for the day, where <input> is either the name or the number of that action
For example `{command} do Bed` or `{command} do 0`""".format(command=commandname)

statustemplate = """
health: {health} / {maxhealth}
coins: {coins}
inventory: []"""


with os.popen("./daclient printinfo", 'r') as infop:
    info = json.load(infop)

with os.popen("./daclient printinput 2>/dev/null", 'r') as inputp:
    _inputs = inputp.read()
inputs = (_inputs + "\n\n").splitlines()[:2]

_action = inputs[1] or info["default"]
if _action in info["options"]:
    action = info["options"][_action]["action"]
    action_valid = info["options"][_action]["available"]
else:
    action = _action
    action_valid = False


invalidactionwarning = "\nWarning: invalid action. Action will probably be changed to {defaultaction}".format(defaultaction=info["default"])

actiontext = """
selected action: {action}{actionvalid}""".format(
    action=action,
    actionvalid=invalidactionwarning if not action_valid else "")

statustext = statustemplate.format(
    health=info["health"],
    maxhealth=info["maxhealth"],
    coins=info["coins"],
    inventory=info.get("inventory", []))

optiontext = """
Possible actions:""" +"".join(
        "\n{number}) {name}: {title} {availability}\n  {description}".format(
            number=number,
            name=name,
            title=option.get("action", ""),
            availability="[UNAVAILABLE]" if not option.get("available") else "",
            description=option.get("description", ""))
        for number, (name, option) in enumerate(sorted(info["options"].items())))

messagestext = "\nMessages:" + "".join("\n    "+message for message in info["messages"])


def set_input(inp):
    try:
        option = sorted(info["options"].items())[int(inp)]
    except ValueError:
        option = inp
    if option not in info["options"] or not info["options"][option]["available"]:
        print("warning: this action is not valid. The action will default to "+info["default"])
    inputstr = inputs[0] + '\n' + option
    with os.popen("./daclient setinput", "w") as inputp:
        inputp.write(inputstr)
    

def main():
    #if sys.argv[1] == "_title"
    #parser = argparse.ArgumentParser(description="Daily Adventure game (frontend)")
    #parser.set_defaults(action="report")
    #subparsers = parser.add_subparsers()
    
    #doparser = subparsers.add_parser("do")
    #doparser.add_argument("input")
    #doparser.set_defaults(action="do")
    
    #def _aap(name):
        #subparser = subparsers.add_parser(name)
        #subparser.set_defaults(action=name)
    #_aap("welcome")
    #_aap("status")
    #_aap("messages")
    #_aap("options")
    #_aap("action")
    #_aap("report")
    ##parser.add_argument("action", nargs='?', default="status", choices=["welcome", "status", "messages", "options", "report"])
    
    #args = parser.parse_args()
    
    #action = args.action
    if len(sys.argv) >= 3:
        action = sys.argv[2]
    else:
        action = "report"
    if action == "welcome":
        print(welcometext)
    elif action == "status":
        print(statustext)
    elif action == "messages":
        print(messagestext)
    elif action == "options":
        print(optiontext)
    elif action == "action":
        print(actiontext)
    elif action == "report":
        print(welcometext)
        print(statustext)
        print(actiontext)
        print(messagestext)
        print(optiontext)
    elif action == "help" or action == "-h" or action == "--help":
        print(helptext)
    elif action == "do":
        set_input(args.input)
        
    
    print("")

if __name__ == "__main__":
    main()
    
