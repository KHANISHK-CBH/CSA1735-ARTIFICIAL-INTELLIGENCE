# Q14. Alpha-Beta pruning algorithm for gaming

def alpha_beta(depth, node_index, is_max, values, max_depth, alpha, beta):
    if depth == max_depth:
        return values[node_index]
    if is_max:
        best = float("-inf")
        for child in (node_index * 2, node_index * 2 + 1):
            best = max(best, alpha_beta(depth + 1, child, False,
                                        values, max_depth, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # beta cut-off
        return best
    best = float("inf")
    for child in (node_index * 2, node_index * 2 + 1):
        best = min(best, alpha_beta(depth + 1, child, True,
                                    values, max_depth, alpha, beta))
        beta = min(beta, best)
        if beta <= alpha:
            break  # alpha cut-off
    return best

if __name__ == "__main__":
    leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]
    result = alpha_beta(0, 0, True, leaf_values, 3,
                        float("-inf"), float("inf"))
    print("Best value for MAX using Alpha-Beta:", result)
