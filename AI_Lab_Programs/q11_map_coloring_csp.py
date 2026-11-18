# Q11. Map Coloring using Constraint Satisfaction (CSP)
# Assign one of three colors so that neighboring regions differ.

def map_coloring():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"]
    }
    colors = ["Red", "Green", "Blue"]
    assignment = {}

    def is_safe(region, color):
        return all(assignment.get(neighbor) != color
                   for neighbor in graph[region])

    def backtrack():
        if len(assignment) == len(graph):
            return True
        # Choose the unassigned region with the most already-assigned neighbors.
        region = max((r for r in graph if r not in assignment),
                     key=lambda r: sum(n in assignment for n in graph[r]))
        for color in colors:
            if is_safe(region, color):
                assignment[region] = color
                if backtrack():
                    return True
                del assignment[region]
        return False

    if backtrack():
        print("Map coloring solution:")
        for region, color in assignment.items():
            print(f"{region} -> {color}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    map_coloring()
