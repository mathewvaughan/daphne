class RoverConnectionLostError(Exception):
    pass


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
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def right(self):
        """Rotate the rover 90 degrees to the right.

        Raises:
            RoverConnectionLostError: _description_
        """
        if not self.connected:
            raise RoverConnectionLostError
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def forward(self):
        """Move the rover forward one grid square.

        Raises:
            RoverConnectionLostError: _description_
        """
        if not self.connected:
            raise RoverConnectionLostError
        if self.direction == "N":
            new_position = [self.position[0], self.position[1] + 1]
        elif self.direction == "E":
            new_position = [self.position[0] + 1, self.position[1]]
        elif self.direction == "S":
            new_position = [self.position[0], self.position[1] - 1]
        elif self.direction == "W":
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
