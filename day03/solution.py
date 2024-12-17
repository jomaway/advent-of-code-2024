# day03.py

from pathlib import Path
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(PATTERN, data)
    return sum([int(op[0]) * int(op[1]) for op in matches])


def part2(data):
    """Solve part 2."""
    PATTERN = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    operations = re.findall(PATTERN, data)
    enabled = True
    result = 0
    for op in operations:
        match op:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                a, b = map(int, op[4:-1].split(","))
                if enabled:
                    result += a * b
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
