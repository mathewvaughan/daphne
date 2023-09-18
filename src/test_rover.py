from src.rover import Rover


def test_reporting_telemetry():
    rover = Rover(position=[0, 0], direction="N")
    assert rover.position == [0, 0]
    assert rover.direction == "N"


def test_turning_left():
    rover = Rover(position=[0, 0], direction="N")
    rover.left()
    assert rover.direction == "W"
    rover.left()
    assert rover.direction == "S"
    rover.left()
    assert rover.direction == "E"
    rover.left()
    assert rover.direction == "N"


def test_turning_right():
    rover = Rover(position=[0, 0], direction="N")
    rover.right()
    assert rover.direction == "E"
    rover.right()
    assert rover.direction == "S"
    rover.right()
    assert rover.direction == "W"
    rover.right()
    assert rover.direction == "N"


def test_moving_forward_north():
    rover = Rover(position=[0, 0], direction="N")
    rover.forward()
    assert rover.position == [0, 1]


def test_moving_forward_east():
    rover = Rover(position=[0, 0], direction="E")
    rover.forward()
    assert rover.position == [1, 0]


def test_moving_forward_south():
    rover = Rover(position=[0, 0], direction="S")
    rover.forward()
    assert rover.position == [0, -1]


def test_moving_forward_west():
    rover = Rover(position=[0, 0], direction="W")
    rover.forward()
    assert rover.position == [-1, 0]
