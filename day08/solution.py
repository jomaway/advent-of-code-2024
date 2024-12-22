# solution for day 8

from pathlib import Path
import sys
from itertools import combinations, permutations

def parse(puzzle_input):
    """Parse input."""
    map = {i+j * 1j: antenna for i, row in enumerate(puzzle_input.split("\n")) for j, antenna in enumerate(row)}
    return map

def part1(data):
    """Solve part 1."""
    return calc_antinodes(data, [1])  

def calc_antinodes(data, factors):
    result = set()
    
    for antenna in {*data.values()} - {'.'}:
        nodes = [key for key, value in data.items() if value == antenna]
        for a,b in permutations(nodes,2):
            for antinode in [a+n*(a-b) for n in factors]:
                if antinode in data:
                    result.add(antinode)

    return len(result)
       

def part2(data):
    """Solve part 2."""
    return calc_antinodes(data,range(50))


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
