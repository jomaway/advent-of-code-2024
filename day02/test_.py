# test_day02.py

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly."""
    assert example == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 2


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 4
