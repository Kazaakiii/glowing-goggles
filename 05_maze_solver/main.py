from collections import deque

MAZE = [
    list("S..#...."),
    list("##.#.##."),
    list("...#..."),
    list(".#####."),
    list("......E"),
]


def find(maze, symbol):
    for row, cells in enumerate(maze):
        for column, cell in enumerate(cells):
            if cell == symbol:
                return row, column
    raise ValueError(f"Maze is missing {symbol}.")


def solve(maze):
    start = find(maze, "S")
    end = find(maze, "E")
    queue = deque([start])
    previous = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        row, column = current
        for neighbor in [(row - 1, column), (row + 1, column),
                         (row, column - 1), (row, column + 1)]:
            next_row, next_column = neighbor
            inside = 0 <= next_row < len(maze) and 0 <= next_column < len(maze[0])
            if inside and maze[next_row][next_column] != "#" and neighbor not in previous:
                previous[neighbor] = current
                queue.append(neighbor)

    if end not in previous:
        return []

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]


def main():
    path = solve(MAZE)
    for row, column in path[1:-1]:
        MAZE[row][column] = "*"
    for row in MAZE:
        print("".join(row))
    print(f"Shortest path length: {len(path) - 1}")


if __name__ == "__main__":
    main()
