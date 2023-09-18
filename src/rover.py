class Rover:
    def __init__(self, position, direction) -> None:
        self.position = position
        self.direction = direction

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
            self.position[1] += 1
        elif self.direction == "E":
            self.position[0] += 1
        elif self.direction == "S":
            self.position[1] -= 1
        elif self.direction == "W":
            self.position[0] -= 1
