# solution for day

from pathlib import Path
import sys
import re

def parse(puzzle_input):
    """Parse input."""
    blocks = puzzle_input.split("\n\n")
    return [[int(num) for num in re.findall("\d+", block)] for block in blocks]
        
def part1(data):
    """Solve part 1."""
    return sum([3*a +b for block in data for a,b in [find_intersections(*block)] if a.is_integer() and b.is_integer()])

def find_intersections(a_x, a_y, b_x, b_y, price_x, price_y):
    a = ((price_x*b_y) - (price_y*b_x)) / ((a_x*b_y)-(a_y*b_x))
    b = (price_y - a_y * a) / b_y
    return a,b
    
def part2(data):
    """Solve part 2."""
    CORRECTION = 10000000000000
    for block in data:
        block[-1] += CORRECTION
        block[-2] += CORRECTION
    return sum([3*a +b for block in data for a,b in [find_intersections(*block)] if a.is_integer() and b.is_integer()])


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
