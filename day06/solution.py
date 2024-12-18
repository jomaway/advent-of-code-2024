# solution for day 6

from pathlib import Path
import sys
from enum import Enum


# Use complex numbers to represent positions
class Direction(Enum):
    NORTH = -1
    EAST = +1j
    SOUTH = +1
    WEST = -1j

    def turn_right(self):
        # rotate 90 degree clockwise
        return Direction(self.value * -1j)


class Guard:
    def __init__(self, pos):
        self.direction = Direction.NORTH
        self.position = pos
        self.path = set()

    def turn_right(self):
        self.direction = self.direction.turn_right()

    def move_forward(self):
        self.position = self.get_next_pos()

    def get_next_pos(self):
        return self.position + self.direction.value

    def move(self, map):
        while self.position in map and not self.is_stuck_in_loop():
            self.path.add((self.position, self.direction))
            pos = self.get_next_pos()
            # if next field is free
            if map.get(pos) in ("#", "O"):
                self.turn_right()
            else:
                self.move_forward()

    def is_stuck_in_loop(self):
        return (self.position, self.direction) in self.path

    def __str__(self):
        return f"{self.position} - {self.direction} #({self.path})"


def parse(puzzle_input):
    """Parse input.
    Returns a dict with the position as complex number as key and the value as char.
    """
    rows = puzzle_input.split("\n")
    map = {i + j * 1j: char for i, row in enumerate(rows) for j, char in enumerate(row)}
    return map


def part1(data):
    """Solve part 1."""
    # find position of the guard
    start = min([key for key, value in data.items() if value == "^"])
    # current direction
    guard = Guard(start)
    guard.move(data)

    return len(set([pos for (pos, _) in guard.path]))


def part2(data):
    """Solve part 2."""
    start = min([key for key, value in data.items() if value == "^"])
    result = 0

    # walk the path once
    guard = Guard(start)
    guard.move(data)

    for pos in {pos for (pos, _) in guard.path}:
        guard = Guard(start)
        guard.move(data | {pos: "#"})
        if guard.is_stuck_in_loop():
            result += 1

    return result


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
