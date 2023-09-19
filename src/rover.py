from pymatrix import Matrix, matrix  # type: ignore


class RoverConnectionLostError(Exception):
    pass


class Grid:
    def __init__(self) -> None:
        self.max_x = 2
        self.max_y = 2
        self.death_points: list[Matrix] = []

    def register_death_point(self, point):
        self.death_points.append(point)

    def is_death_point(self, point):
        return point in self.death_points


NORTH = matrix([[0], [1]])
EAST = matrix([[1], [0]])
SOUTH = matrix([[0], [-1]])
WEST = matrix([[-1], [0]])

TURN_LEFT = matrix([[0, -1], [1, 0]])
TURN_RIGHT = matrix([[0, 1], [-1, 0]])


class Rover:
    def __init__(self, position, direction, grid) -> None:
        self.position = position
        self.direction = direction
        self.grid = grid
        self.connected = True

    def left(self):
        """Rotate the rover 90 degrees to the left.

        Raises:
            RoverConnectionLostError: _description_
        """
        if not self.connected:
            raise RoverConnectionLostError
        self.direction = TURN_LEFT * self.direction

    def right(self):
        """Rotate the rover 90 degrees to the right.

        Raises:
            RoverConnectionLostError: _description_
        """
        if not self.connected:
            raise RoverConnectionLostError
        self.direction = TURN_RIGHT * self.direction

    def forward(self):
        """Move the rover forward one grid square.

        Raises:
            RoverConnectionLostError: _description_
        """
        if not self.connected:
            raise RoverConnectionLostError
        new_position = self.position + self.direction
        if self.grid.is_death_point(new_position):
            return
        if (
            new_position[0][0] > self.grid.max_x
            or new_position[1][0] > self.grid.max_y
            or new_position[0][0] < 0
            or new_position[1][0] < 0
        ):
            self.connected = False
            self.grid.register_death_point(new_position)
            return
        self.position = new_position
