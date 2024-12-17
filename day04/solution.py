# solution for day 4

from pathlib import Path
import sys
import numpy as np


def parse(puzzle_input):
    """Parse input."""
    rows = puzzle_input.split("\n")
    return np.array([list(row) for row in rows])


def part1(data):
    """Solve part 1."""
    xmas_count = 0
    # search rows
    for row in data:
        xmas_count += count_xmas(row)
    # search columns (rows of the transposed matrix)
    for row in data.T:
        xmas_count += count_xmas(row)
    # search diagonals
    flipped = np.fliplr(data)  # flip for anti-diagonals
    for idx in range(len(data) - 3):
        xmas_count += count_xmas(np.diag(data, k=idx))
        xmas_count += count_xmas(np.diag(flipped, k=idx))
        if idx != 0:
            xmas_count += count_xmas(np.diag(data, k=-idx))
            xmas_count += count_xmas(np.diag(flipped, k=-idx))
    return xmas_count


def count_xmas(row):
    xmas_count = 0
    for i in range(len(row) - 3):
        slice = "".join(row[i : i + 4])
        if slice == "XMAS" or slice == "SAMX":
            xmas_count += 1
    return xmas_count


def part2(data):
    """Solve part 2."""
    xmas_count = 0
    # Get all 3x3 subarrays
    n_rows, n_cols = data.shape
    for row in range(n_rows - 2):
        for col in range(n_cols - 2):
            subarray = data[row : row + 3, col : col + 3]
            if is_valid_xmas(subarray):
                xmas_count += 1
    return xmas_count


def is_valid_xmas(data):
    diag1 = "".join(np.diag(data))
    diag2 = "".join(np.diag(np.fliplr(data)))
    return diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM")


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
