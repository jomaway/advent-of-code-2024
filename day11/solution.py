# solution for day 11

from pathlib import Path
from collections import deque 
import sys


def parse(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.strip().split()))


def part1(data):
    """Solve part 1."""
    stones = {nr:1 for nr in data}
    for _ in range(25):
        stones = blink(stones)

    return sum(stones.values())


def apply_rule(stone) -> list:
    if stone == 0:
        return [1,]
    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    
    return [stone * 2024,]

def blink(stones: dict):
    new_stones = {} 
    for stone in stones.keys():
        numbers = apply_rule(stone)
        for nr in numbers:
            if new_stones.get(nr) is None:
                new_stones[nr] = 0
            
            new_stones[nr] += stones[stone]
    return new_stones

def part2(data):
    """Solve part 2."""
    stones = {i: 1 for i in data}
    for _ in range(75):
        stones = blink(stones)
        
    return sum(stones.values())


def solve(puzzle_input):
    """Solve the puzzle fo the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
