# day01.py

from pathlib import Path
import sys

def parse(puzzle_input):
    """Parse input."""
    # line = [[int(x) for x in line.split()] for line in puzzle_input.split("\n")]
    line = [line.split() for line in puzzle_input.split("\n")]
    first, second = [list(map(int,x)) for x in zip(*line)]
    return first, second

def part1(data):
    """Solve part 1."""
    first, second = data
    diffs = [abs(a - b) for a,b in zip(sorted(first), sorted(second))]
    return sum(diffs)

def part2(data):
    """Solve part 2."""
    first, second = data
    similarities = [value * second.count(value) for value in first]
    return sum(similarities)

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
