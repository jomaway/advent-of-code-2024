# solution for day 5

from pathlib import Path
import sys
import itertools


def parse(puzzle_input):
    """Parse input."""
    rules, updates = puzzle_input.split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [tuple(map(int, update.split(","))) for update in updates.split("\n")]
    return rules, updates


def part1(data):
    """Solve part 1."""
    rules, updates = data
    result = 0
    for update in updates:
        combinations = list(itertools.combinations(update, 2))
        if all([comb in rules for comb in combinations]):
            result += update[int(len(update) / 2)]
    return result


def part2(data):
    """Solve part 2."""
    rules, updates = data
    result = 0

    for update in updates:
        combinations = list(itertools.combinations(update, 2))
        if not all([comb in rules for comb in combinations]):
            fixed_update = fix_update(update, rules)
            result += fixed_update[int(len(fixed_update) / 2)]

    return result


def fix_update(pages, rules):
    in_degree = {number: 0 for number in pages}

    # get the number of inputs for each page number
    for u, v in rules:
        if u in in_degree and v in in_degree:
            in_degree[v] += 1

    # return ordered pages.
    return [k for k, _ in sorted(in_degree.items(), key=lambda item: item[1])]


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
