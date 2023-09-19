from dataclasses import dataclass

from pymatrix import matrix  # type: ignore

from src.rover import Grid, Rover

FORWARD = "F"
LEFT = "L"
RIGHT = "R"


def translate_direction_to_vector(direction):
    if direction == "N":
        return matrix([[0], [1]])
    if direction == "E":
        return matrix([[1], [0]])
    if direction == "S":
        return matrix([[0], [-1]])
    return matrix([[-1], [0]])


@dataclass
class World:
    grid: Grid
    rovers: list[Rover]
    commands: dict[Rover, list[str]]


def build_world(command) -> World:
    """Build a world from a command string.

    Args:
        command (str): The command string for the system

    Returns:
        _type_: World
    """
    lines = command.split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    grid_dimensions = lines[0].split(" ")
    grid = Grid(int(grid_dimensions[0]), int(grid_dimensions[1]))
    rovers = []
    commands = {}
    for i in range(1, len(lines), 2):
        telemetry = lines[i].split(" ")
        position = matrix([[int(telemetry[0])], [int(telemetry[1])]])
        direction = translate_direction_to_vector(telemetry[2])
        rover = Rover(position, direction, grid)
        commands[rover] = [*lines[i + 1]]
        rovers.append(rover)
    return World(grid, rovers, commands)
