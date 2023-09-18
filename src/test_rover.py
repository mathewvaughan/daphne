import pytest

from src.rover import Rover


class Grid:
    def __init__(self) -> None:
        self.max_x = 2
        self.max_y = 2


@pytest.fixture(name="rover")
def rover_fixture():
    return Rover(position=[1, 1], direction="N", grid=Grid())


def test_reporting_telemetry():
    rover = Rover(position=[0, 0], direction="N", grid=Grid())
    assert rover.position == [0, 0]
    assert rover.direction == "N"


def test_turning_left(rover):
    rover.left()
    assert rover.direction == "W"
    rover.left()
    assert rover.direction == "S"
    rover.left()
    assert rover.direction == "E"
    rover.left()
    assert rover.direction == "N"


def test_turning_right(rover):
    rover.right()
    assert rover.direction == "E"
    rover.right()
    assert rover.direction == "S"
    rover.right()
    assert rover.direction == "W"
    rover.right()
    assert rover.direction == "N"


def test_moving_forward_north(rover):
    rover.forward()
    assert rover.position == [1, 2]


def test_moving_forward_east(rover):
    rover.right()
    rover.forward()
    assert rover.position == [2, 1]


def test_moving_forward_south(rover):
    rover.right()
    rover.right()
    rover.forward()
    assert rover.position == [1, 0]


def test_moving_forward_west(rover):
    rover.left()
    rover.forward()
    assert rover.position == [0, 1]


# def test_pushing_to_edge_of_grid_north(rover):
#     with pytest.raises(RoverConnectionLostError):
#         rover.forward()
#         rover.forward()
