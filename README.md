# Daphne Tech Test

Challenge instructions can be found in `SPEC.md`.

## Installation

Make sure you have poetry installed and run:

`poetry install`

This will install project dependencies locally in the root directory.

To run the tests run:

`poetry run task test`

## Working Notes

I'm going to approach this task in a few stages.

1. Implement the rover. It initially will have an interface that allows turning Left, Right and moving Forward. I'm aware that the tech task mentions that these commands may need to be more flexible in future, but I don't need that just yet. I will add some thoughts on this at the end of the task. The rover will move freely in an infinite plane and we will be able to ask it for its current position. Be free, my martian friend.
1. Implement a grid. The rover will take in a grid and collaborate with it to track its movement. We will be able to ask the rover for its position within its grid. At this stage, the injected grid will always be 3x3 grid and the starting coordinates will be fixed at 2,2. We'll use this grid to guide our edge case (pun intended) behaviours.
1. Rover death.
1. Rover death avoidance.
1. Top level orchestrator that can translate the string commands into useful actions for our interfaces, allowing new starting positions and grid shapes!
1. Review


TODO:
Talk about extending interface of the rover to allow more flexible commands.
