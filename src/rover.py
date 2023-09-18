from pymatrix import matrix  # type: ignore


class RoverConnectionLostError(Exception):
    pass


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
        if self.direction == NORTH:
            new_position = [self.position[0], self.position[1] + 1]
        elif self.direction == EAST:
            new_position = [self.position[0] + 1, self.position[1]]
        elif self.direction == SOUTH:
            new_position = [self.position[0], self.position[1] - 1]
        elif self.direction == WEST:
            new_position = [self.position[0] - 1, self.position[1]]
        if (
            new_position[0] > self.grid.max_x
            or new_position[1] > self.grid.max_y
            or new_position[0] < 0
            or new_position[1] < 0
        ):
            self.connected = False
            return
        self.position = new_position
