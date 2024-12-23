# solution for day 10

from pathlib import Path
import sys


def parse(puzzle_input):
    """Parse input."""
    map = {i+j*1j: int(height) for i, row in enumerate(puzzle_input.split("\n")) for j, height in enumerate(row)}
    return map


def part1(map):
    """Solve part 1."""
    trailheads = [key for key, value in map.items() if value == 0]
    graph = build_graph(map)
    return sum(find_num_trails(map, graph,trailhead) for trailhead in trailheads)


def build_graph(map):
    graph = {}

    for pos, value in map.items():
        graph[pos] = []

        for direction in [1,-1,1j,-1j]:
            neighbor = pos + direction

            if neighbor in map and map[neighbor] - value == 1:
                graph[pos].append(neighbor)

    return graph 

def find_num_trails(map, graph, start):
    trails = set()

    def dfs(node, path):
        path.append(node)

        if map[node] == 9:
            trails.add(node)
            # print(f"P: {path}")
        else:
            for next in graph[node]:
                if next not in path:
                    dfs(next,path)

        path.pop()

    dfs(start, [])
    return len(trails)
         

def part2(data):
    """Solve part 2."""
    pass


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
