# solution for day

from pathlib import Path
import sys
import re
from collections import Counter

def parse(input):
    """Parse input. Use complex numbers as position and velocity"""
    robots = [[int(x) for x in re.findall("[+-]?\d+", robot)] for robot in input.split("\n")]
    return [(complex(*robot[:2]), complex(*robot[2:])) for robot in robots]


WIDTH = 101
HEIGHT = 103


class Robot:
    def __init__(self, position, velocity):
        self.pos = position
        self.velo = velocity

    @property
    def x(self):
        return self.pos.real

    @property
    def y(self):
        return self.pos.imag

    def move(self):
        self.pos += self.velo
        self.teleport()

    def teleport(self):
        "only teleports if neccesairy"
        x = self.pos.real
        y = self.pos.imag

        if x < 0:
            self.pos += WIDTH
        elif x >= WIDTH:
            self.pos -= WIDTH
        if y < 0:
            self.pos += HEIGHT * 1j
        elif y >= HEIGHT:
            self.pos -= HEIGHT * 1j

    def run(self, steps = 100, debug = False):
        for i in range(steps):
            self.move()
            if debug:
                print(f"{i}: {self}")

        return self.quadrant()

    def __str__(self):
        return f"{self.pos}"

    def quadrant(self):
        center_y = HEIGHT // 2
        center_x = WIDTH // 2
        if self.x < center_x and self.y < center_y:
            return 1
        if self.x < center_x and self.y > center_y:
            return 2
        if self.x > center_x and self.y < center_y:
            return 4
        if self.x > center_x and self.y > center_y:
            return 3
        # Implicitly returns None if on the center axes 
       
def part1(robots):
    """Solve part 1."""
    counts = Counter(Robot(*value).run() for value in robots)
    return counts[1] * counts[2] * counts[3] * counts[4]


def part2(robots):
    """Solve part 2."""


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
