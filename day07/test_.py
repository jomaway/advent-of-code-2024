# test for day 7

import pathlib
import pytest
import solution as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == ...


def test_part1_example(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 3749


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 11387