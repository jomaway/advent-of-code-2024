# solution for day 6

from pathlib import Path
import sys
import numpy as np
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


DIRECTION_DELTAS = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1),
}


class Guard:
    def __init__(self, pos):
        self.direction = Direction.NORTH
        self.position = pos
        self.path = set()
        self.path.add((pos, self.direction))
        self.escaped = False
        self.stuck_in_loop = False

    def turn_right(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def move_forward(self):
        self.position = self.get_next_pos()
        if (self.position, self.direction) in self.path:
            self.stuck_in_loop = True
        else:
            self.path.add((self.position, self.direction))

    def get_next_pos(self):
        delta = DIRECTION_DELTAS[self.direction]
        return (self.position[0] + delta[0], self.position[1] + delta[1])

    def is_next_field_free(self, map):
        row, col = self.get_next_pos()
        # check if next field is outside of map
        n_rows, n_cols = map.shape
        if not (0 <= row < n_rows and 0 <= col < n_cols):
            self.escaped = True
            return False  # return false so that guard is not moving anymore.
        # return not map[row][col] == "#"
        return map[row][col] not in ("#", "O")

    def move(self, map):
        if self.is_next_field_free(map):
            self.move_forward()
        else:
            self.turn_right()

    def is_escaped(self):
        return self.escaped

    def is_stuck_in_loop(self):
        return self.stuck_in_loop

    def __str__(self):
        return f"{self.position} - {self.direction} #({self.path})"


def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.split("\n")
    return np.array([list(row) for row in rows])


def part1(data):
    """Solve part 1."""
    # find position of the guard
    start = tuple(int(val[0]) for val in np.where("^" == data))  # (row,col)
    # current direction
    guard = Guard(start)
    while not guard.is_escaped():
        guard.move(data)

    return len(set([pos for (pos, _) in guard.path]))


def part2(data):
    """Solve part 2."""
    start = tuple(int(val[0]) for val in np.where("^" == data))  # (row,col)
    result = 0

    # get path from guard.
    guard = Guard(start)
    while not guard.is_escaped():
        guard.move(data)

    for pos in set([pos for (pos, _) in guard.path]):
        result += process_guard_path(start, pos[0], pos[1], data)

    return result


def process_guard_path(start, ri, ci, data):
    map = data.copy()
    map[ri][ci] = "O"

    guard = Guard(start)
    while True:
        guard.move(map)
        if guard.is_stuck_in_loop():
            return 1
        if guard.is_escaped():
            return 0


def solve(puzzle_input):
    """Solve the puzzle fo the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
