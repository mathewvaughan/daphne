import pytest

from src.rover import Rover


@pytest.fixture(name="rover")
def rover_fixture():
    return Rover(position=[0, 0], direction="N")


def test_reporting_telemetry():
    rover = Rover(position=[0, 0], direction="N")
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
    assert rover.position == [0, 1]


def test_moving_forward_east(rover):
    rover.right()
    rover.forward()
    assert rover.position == [1, 0]


def test_moving_forward_south(rover):
    rover.right()
    rover.right()
    rover.forward()
    assert rover.position == [0, -1]


def test_moving_forward_west(rover):
    rover.left()
    rover.forward()
    assert rover.position == [-1, 0]
