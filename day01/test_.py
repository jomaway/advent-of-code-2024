# test_day01.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 11


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 31
