class RoverConnectionLostError(Exception):
    pass


class Rover:
    def __init__(self, position, direction, grid) -> None:
        self.position = position
        self.direction = direction
        self.grid = grid

    def left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def forward(self):
        if self.direction == "N":
            new_position = [self.position[0], self.position[1] + 1]
        elif self.direction == "E":
            new_position = [self.position[0] + 1, self.position[1]]
        elif self.direction == "S":
            new_position = [self.position[0], self.position[1] - 1]
        elif self.direction == "W":
            new_position = [self.position[0] - 1, self.position[1]]
        self.position = new_position
