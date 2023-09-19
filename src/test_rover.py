import pytest
from pymatrix import matrix  # type: ignore

from src.rover import EAST, NORTH, SOUTH, WEST, Grid, Rover, RoverConnectionLostError


@pytest.fixture(name="grid")
def grid_fixture():
    return Grid()


@pytest.fixture(name="rover")
def rover_fixture(grid):
    return Rover(position=matrix([[1], [1]]), direction=NORTH, grid=grid)


def test_reporting_telemetry(grid):
    rover = Rover(position=matrix([[0], [0]]), direction=NORTH, grid=grid)
    assert rover.position == matrix([[0], [0]])
    assert rover.direction == NORTH


def test_turning_left(rover):
    rover.left()
    assert rover.direction == WEST
    rover.left()
    assert rover.direction == SOUTH
    rover.left()
    assert rover.direction == EAST
    rover.left()
    assert rover.direction == NORTH


def test_turning_right(rover):
    rover.right()
    assert rover.direction == EAST
    rover.right()
    assert rover.direction == SOUTH
    rover.right()
    assert rover.direction == WEST
    rover.right()
    assert rover.direction == NORTH


def test_moving_forward_north(rover):
    rover.forward()
    assert rover.position == matrix([[1], [2]])


def test_moving_forward_east(rover):
    rover.right()
    rover.forward()
    assert rover.position == matrix([[2], [1]])


def test_moving_forward_south(rover):
    rover.right()
    rover.right()
    rover.forward()
    assert rover.position == matrix([[1], [0]])


def test_moving_forward_west(rover):
    rover.left()
    rover.forward()
    assert rover.position == matrix([[0], [1]])


def test_pushing_to_edge_of_grid_north(rover):
    rover.forward()
    rover.forward()
    assert rover.connected is False
    assert rover.position == matrix([[1], [2]])


def test_if_rover_dead_it_cannot_receieve_another_command(rover):
    rover.forward()
    rover.forward()
    assert rover.connected is False
    with pytest.raises(RoverConnectionLostError):
        rover.forward()
    with pytest.raises(RoverConnectionLostError):
        rover.left()
    with pytest.raises(RoverConnectionLostError):
        rover.right()


def test_second_rover_ignores_suicidal_command(grid):
    rover = Rover(position=matrix([[2], [2]]), direction=NORTH, grid=grid)
    rover2 = Rover(position=matrix([[2], [1]]), direction=NORTH, grid=grid)
    rover.forward()
    assert rover.connected is False
    rover2.forward()
    rover2.forward()
    assert rover2.position == matrix([[2], [2]])
    assert rover2.connected is True
    rover2.left()
    rover2.forward()
    assert rover2.position == matrix([[1], [2]])
