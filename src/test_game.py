from pymatrix import matrix  # type: ignore

from src.game import FORWARD, LEFT, RIGHT, build_world, generate_report
from src.rover import EAST, NORTH, Grid, Rover

input_command = """
5 3 

1 1 E 
RFRFRFRF

3 2 N 
FRRFLLFFRRFLL

0 3 W
LLFFFLFLFL
"""

output = """
1 1 E
3 3 N LOST
2 3 S
"""


def test_world_builder():
    command = """
    1 1
    
    1 1 E
    LRF
    """
    result = build_world(command)
    assert result.grid.max_x == 1
    assert result.grid.max_y == 1
    rover = result.rovers[0]
    assert rover.grid == result.grid
    assert rover.position == matrix([[1], [1]])
    assert rover.direction == EAST
    assert result.commands[rover] == [LEFT, RIGHT, FORWARD]


def test_reporter():
    grid = Grid(1, 1)
    rover1 = Rover(position=matrix([[0], [0]]), direction=NORTH, grid=grid)
    lost_rover = Rover(position=matrix([[0], [0]]), direction=NORTH, grid=grid)
    rover1.forward()
    lost_rover.forward()
    lost_rover.forward()
    assert generate_report([rover1, lost_rover]) == "0 1 N\n0 1 N LOST\n"
