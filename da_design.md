


# Description

Daily adventure is an rpg.
It is somewhat inspired by idle games like candybox.

During the day all players send their inputs to the central program.
At UTC midnight this program will read the inputs from all players and execute the actions.

After this execution the program will list the possible actions for the player.
Some unavailable actions will also be listed, with the reason why they are unavailable.

## Actions

Per day players can perform 2 actions.
 - One smaller action: the morning action
 - One bigger action: the afternoon action

### Morning action

The morning actions are smaller actions.
Examples would be buying an item or starting a party

### Afternoon action

This is a larger action; indicated by the place to go.
Examples can be to enter a dungeon, to rest a while to regain health, to work somewhere or to join a party and do whatever the party leader has chose


# Design pseudocode

// noon
input <- read_input()
state <- load_saved_state()
actions <- validate_and_set_input(input, state)
// evening
state <- update(state, actions)
save_state(state)
// morning
display_state(state)
