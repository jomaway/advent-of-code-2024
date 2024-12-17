set quiet

# alias
self := justfile_dir()
venv := self / ".venv"

[private]
default:
    just --list

# run solution for a given day - file can be input | example
run file day:
    #!/usr/bin/env bash
    set -euo pipefail # Exit on error
    DAY=$(printf "%02d" {{day}})
    uv run day${DAY}/solution.py day${DAY}/{{file}}.txt

# run tests for a given day x.
test day:
    #!/usr/bin/env bash
    set -euo pipefail # Exit on error
    DAY=$(printf "%02d" {{day}})
    pytest day${DAY}

# activate the virtual environment
activate-venv:
    source {{venv}}/bin/activate

# scafold template for the day x
scafold day:
    #!/usr/bin/env bash
    set -euo pipefail # Exit on error
    DAY=$(printf "%02d" {{day}})
    DIRECTORY={{self}}/day${DAY}
    # check if does not exists.
    if [ ! -d "$DIRECTORY" ]; then
        cp -r {{self}}/template $DIRECTORY
        touch $DIRECTORY/example.txt
        # download input
        source .env
        curl -o $DIRECTORY/input.txt https://adventofcode.com/2024/day/{{day}}/input --cookie "session=$AOC_SESSION_COOKIE"
    else
        echo "Day {{day}} already exist."
    fi
