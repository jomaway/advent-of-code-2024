# solution for day 07

from pathlib import Path
import sys


def parse(puzzle_input):
    """Parse input."""
    tests = [[part for part in line.split(":")] for line in puzzle_input.split("\n")]                
    tests = [(int(test[0]), list(map(int,test[1].split()))) for test in tests]
    return tests

    
def part1(data):
    """Solve part 1."""
    return sum(answer for answer, numbers in data if evaluate(answer,numbers))

def evaluate(answer, numbers, is_part2 = False):
    if len(numbers) >= 2:
        return evaluate(answer,[sum(numbers[:2]), *numbers[2:]],is_part2) or evaluate(answer,[numbers[0] * numbers[1], *numbers[2:]], is_part2) or (evaluate(answer, [int(str(numbers[0]) + str(numbers[1])), *numbers[2:]], is_part2) if is_part2 else False)
    else:
        return answer == numbers[0]
     
def part2(data):
    """Solve part 2."""
    return sum(answer for answer,numbers in data if evaluate(answer,numbers,True))

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
