# solution for day 12

from pathlib import Path
import sys
from itertools import combinations


def parse(puzzle_input):
    """Parse input."""
    return {
        i + j * 1j: plant
        for i, row in enumerate(puzzle_input.split("\n"))
        for j, plant in enumerate(row)
    }


class plot:
    def __init__(self, pos, plant):
        self.position = pos
        self.plant = plant
        self.fences = 0
        self.area = None


def part1(data):
    """Solve part 1."""
    areas = []

    seen = set()
    for pos, plant in data.items():
        if pos not in seen:
            areas.append(find_area(pos, plant, data, seen))

    return sum(map(lambda area: area["fences"] * len(area["plots"]), areas))


def neighbors(pos):
    return (pos + 1, pos - 1, pos + 1j, pos - 1j)


def fences(pos, map):
    return sum([1 for n in neighbors(pos) if n not in map or map[pos] != map[n]])


def corners(pos, map):
    plant = map[pos]
    outside, inside = [], []
    for n in neighbors(pos):
        if n not in map or plant != map.get(n):
            outside.append(n)
        else:
            inside.append(n)
    outer = sum([1 for a, b in combinations(outside, 2) if abs(a - b) == 2 ** (1 / 2)])
    inner = sum(
        [
            1
            for a, b in combinations(inside, 2)
            if abs(a - b) == 2 ** (1 / 2) and map[(2 * a - pos) + (b - a)] != plant
        ]
    )
    return outer + inner


def find_area(start, plant, map, seen):
    stack = [start]
    area = {"fences": 0, "plots": set(), "corners": 0}
    while stack:
        pos = stack.pop()
        if pos in seen or pos not in map or map[pos] != plant:
            continue
        seen.add(pos)
        area["plots"].add(pos)
        area["fences"] += fences(pos, map)
        area["corners"] += corners(pos, map)
        stack.extend(neighbors(pos))
    return area


def part2(data):
    """Solve part 2."""
    areas = []

    seen = set()
    for pos, plant in data.items():
        if pos not in seen:
            areas.append(find_area(pos, plant, data, seen))

    return sum(map(lambda area: area["corners"] * len(area["plots"]), areas))


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
