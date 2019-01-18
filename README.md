
# Daily Adventure

Daily Adventure is a small game where you can choose an action for each day.

## Usage

On tilde.town, tilde.institute or other places where it is set up, you can run `da` or `/home/troido/bin/da` to see the current report for you character.

You can choose an action using command line arguments, for example `da do bed` or `da do 0`

The game will update on UTC midnight; after that you will have to select another action for the next day

## Setup

Someday I will make an install script...

### updater

The first step is to make the `data/` directory in the `daily_adventure/` directory.
Then you have to run `updater/main.py new` to initialize the world.

In order to run it each day you should add the following line to your crontab (with the paths changed to where you have daily adventure installed):

    0 0 * * * /home/troido/daily_adventure/updater/main.py >>/home/troido/daily_adventure/da.stdout.log 2>>/home/troido/daily_adventure/da.stderr.log

### client

You should compile `client/daclient.c`. The compiled file should be `client/daclient`.
You should give this compiled file the setuid permissions: `chmod 6755 client/daclient`.

You should symlink `client/data` to `data/`.

In order to run it as command you should copy `client/da` to some directory in your `$PATH` and change ``"`dirname $0`"`` into the path for `client/`.
