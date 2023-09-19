from pymatrix import matrix  # type: ignore

from src.game import FORWARD, LEFT, RIGHT, build_world
from src.rover import EAST

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
