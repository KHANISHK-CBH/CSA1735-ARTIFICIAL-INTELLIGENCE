# Q13. Minimax algorithm for a gaming problem
# Demonstration using a small game tree (leaf values are utilities).

def minimax(depth, node_index, is_max, values, max_depth):
    if depth == max_depth:
        return values[node_index]
    if is_max:
        return max(minimax(depth + 1, node_index * 2, False, values, max_depth),
                   minimax(depth + 1, node_index * 2 + 1, False, values, max_depth))
    return min(minimax(depth + 1, node_index * 2, True, values, max_depth),
               minimax(depth + 1, node_index * 2 + 1, True, values, max_depth))

if __name__ == "__main__":
    leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]
    depth = 3
    print("Leaf values:", leaf_values)
    print("Best value for MAX:", minimax(0, 0, True, leaf_values, depth))
