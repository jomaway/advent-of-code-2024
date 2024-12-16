# test_day02.py

import pathlib
import pytest
import day02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent / "data"


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example02.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 4
