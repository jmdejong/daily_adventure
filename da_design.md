



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
