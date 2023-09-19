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


def translate_vector_direction_to_string(direction):
    if direction == matrix([[0], [1]]):
        return "N"
    if direction == matrix([[1], [0]]):
        return "E"
    if direction == matrix([[0], [-1]]):
        return "S"
    return "W"


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
        World: World
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


def generate_report(rovers: list[Rover]):
    result = ""
    for rover in rovers:
        position = str(rover.position).replace("\n", " ")
        direction = translate_vector_direction_to_string(rover.direction)
        telemetry_line = f"{position} {direction}"
        if not rover.connected:
            telemetry_line = telemetry_line + " LOST"
        result = result + telemetry_line + "\n"
    return result


def run_game(command_string):
    """Runs the game from a command string.

    Args:
        command (str): The command string for the system


    Returns:
        str: User friendly output of the game
    """
    world = build_world(command_string)
    for rover in world.rovers:
        for command in world.commands[rover]:
            if not rover.connected:
                break
            if command == FORWARD:
                rover.forward()
            elif command == LEFT:
                rover.left()
            else:
                rover.right()
    return generate_report(world.rovers)
