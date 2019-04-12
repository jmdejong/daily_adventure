#!/usr/bin/env python3 

"""
There are several ways to start the program:

The preferred way is to go to the root git directory and run `python3 -m dailyadventure`.

Alternative ways are running `python3 dailyadventure/` from the git root, or `python3 .` from the dailyadventure dir
You can also explicitly execute __main__.py using `python3 __main__.py` or `./__main__.py`
"""

import sys

if sys.version_info[0] < 3:
    print("Error: this program is written in python 3. You are trying to run it in python 2")
    sys.exit(-1)

if __package__ != "dailyadventure":
    import os.path

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dailyadventure.main import main

main()
