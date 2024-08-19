import heapq


def find_total_distance(warehouse, targets, walkable_tile):
    # Define possible moves: up, down, left, and right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < len(warehouse) and 0 <= y < len(warehouse[0]) and warehouse[x][y] == walkable_tile

    def heuristic(node, target):
        return abs(node[0] - target[0]) + abs(node[1] - target[1])

    def astar(start, target):
        open_list = []
        heapq.heappush(open_list, (0, start))
        g_scores = {start: 0}

        while open_list:
            _, current = heapq.heappop(open_list)
            if current == target:
                return g_scores[current]

            for dx, dy in moves:
                new_x, new_y = current[0] + dx, current[1] + dy
                new_node = (new_x, new_y)

                if is_valid(new_x, new_y):
                    tentative_g_score = g_scores[current] + 1
                    if new_node not in g_scores or tentative_g_score < g_scores[new_node]:
                        g_scores[new_node] = tentative_g_score
                        f_score = tentative_g_score + \
                            heuristic(new_node, target)
                        heapq.heappush(open_list, (f_score, new_node))

        return -1  # If no path is found

    total_distance = 0
    current_location = (0, 0)  # Starting point
    for target in targets:
        distance = astar(current_location, target)
        if distance == -1:
            return -1  # If there's no path to a target, return -1
        total_distance += distance
        current_location = target

    return total_distance
