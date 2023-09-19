# Daphne Tech Test

Challenge instructions can be found in `SPEC.md`.

## Installation

Make sure you have poetry installed and run:

`poetry install`

This will install project dependencies locally in the root directory.

To run the tests run:

`poetry run task test`

If you want to double check this meets the spec, theres an integration test in 'test_game' using the same input/output strings provided in the spec.

## Approach

I'm going to approach this task in a few stages.

1. Implement the rover. It initially will have an interface that allows turning Left, Right and moving Forward. I'm aware that the tech task mentions that these commands may need to be more flexible in future, but I don't need that just yet. I will add some thoughts on this at the end of the task. The rover will move freely in an infinite plane and we will be able to ask it for its current position. Be free, my martian friend. ✅
1. Implement a grid. The rover will take in a grid and collaborate with it to track its movement. We will be able to ask the rover for its position within its grid. At this stage, the injected grid will always be 3x3 grid and the starting coordinates will be fixed at 2,2. We'll use this grid to guide our edge case (pun intended) behaviours. ✅
1. Rover death. ✅
1. Handling sequential rovers ✅
1. Rover death avoidance. ✅
1. Top level orchestrator that can translate the string commands into useful actions for our interfaces, allowing new starting positions and grid shapes! ✅
1. Review ✅

Working Notes:
- I've got to the stage where I need to implement death avoidance. I know that the grid will need to track the last known position of dead rovers, so I'm about to start cleaning up the responsibilities of the two objects a little bit. One thing I don't really like so far is how I've used strings to represent directions. I can simplify a lot of the implementation by using vectors/matrices. Along those same lines I don't think the interface of the rover should return strings either, so I'm going to switch up how the telemetry is returned to the caller as well as the underlying implementation. After these two refactors it should be clearer how to implement sequential rovers and rover death.


Review:
- Firstly to address increased flexibility of commands I've modelled positions and directions with matrices and vectors which provides a basis for their extension. One caveat is the death avoidance currently depends on the 'would be' position of the vehicle if it had not lost connection; if we had more flexible mechanics then this wouldn't be sufficient for death avoidance of subsequent rovers.
- I've separated the creation of the game world, report and orchestration of the game at the top level, and modelled the core concepts separately from these still. 
- I'm a big fan of this kata, btw!

Hope you have enjoyed my submission!