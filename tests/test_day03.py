# test_day03.py

import pathlib
import pytest
import day03 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent / "data"


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example03.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly."""
    assert (
        example
        == "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )


def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 161


def test_part2_example1(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 48
