# day02.py

from pathlib import Path
import sys


def parse(puzzle_input):
    """Parse input."""
    reports = puzzle_input.split("\n")
    reports = [[int(x) for x in level.split()] for level in reports]
    return reports


def part1(data):
    """Solve part 1."""
    results = sum([1 for report in data if check_safety(report)])
    return results


def part2(data):
    """Solve part 2."""
    result = 0
    for report in data:
        if check_safety(report):
            result += 1
        else:
            for i in range(len(report)):
                sub_report = report[:i] + report[i + 1 :]
                if check_safety(sub_report):
                    result += 1
                    break

    return result


def check_safety(report):
    """Check the safety of a report by the following rules:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    diffs = [level - report[idx + 1] for idx, level in enumerate(report[:-1])]
    if (all(x > 0 for x in diffs) or all(x < 0 for x in diffs)) and all(
        abs(x) <= 3 for x in diffs
    ):
        return True
    return False


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
