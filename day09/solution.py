# solution for day

from pathlib import Path
import sys


def parse(puzzle_input):
    """Parse input."""
    disk = []
    for idx, value in enumerate(puzzle_input.strip("\n")):
        if idx % 2 == 0: # file
            disk.extend([int(idx/2),] * int(value))
        else: # free
            disk.extend(['.'] * int(value))
    return disk

def calc_checksum(data):
    return sum(int(value) * idx for idx, value in enumerate(data) if value != '.')

def part1(data):
    """Solve part 1."""
    dots = [idx for idx, val in enumerate(data) if val == '.']
    dots = [val for val in dots if val < len(data) - len(dots)]

    
    for idx in dots:
        while data[-1] == '.':
            data.pop()
        data[idx] = data.pop()


    return calc_checksum(data)


def part2(data):
    """Solve part 2."""
    for file_id in range(data[-1], -1,-1):
        max_idx = len(data) - data[::-1].index(file_id) - 1
        min_idx = data.index(file_id)
        size = max_idx - min_idx + 1
        if find_and_replace(data, [file_id] * size, min_idx):
            data[min_idx:max_idx+1] = ['.'] * size

    return calc_checksum(data)
 
def find_and_replace(data, file, idx):
    x = len(file)
    target = ['.'] * x
    
    for i in range(idx):
        if data[i:i+x] == target:
            data[i:i+x] = file
            return True
    return False
            
 
 
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
