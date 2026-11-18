# Q15. Decision Tree classification using ID3 (information gain)
# Small sample dataset: decide whether to play based on weather.

from math import log2
from collections import Counter, defaultdict

data = [
    ({"Outlook": "Sunny", "Wind": "Weak"}, "No"),
    ({"Outlook": "Sunny", "Wind": "Strong"}, "No"),
    ({"Outlook": "Overcast", "Wind": "Weak"}, "Yes"),
    ({"Outlook": "Rain", "Wind": "Weak"}, "Yes"),
    ({"Outlook": "Rain", "Wind": "Strong"}, "No"),
    ({"Outlook": "Overcast", "Wind": "Strong"}, "Yes"),
]

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((count / total) * log2(count / total)
                for count in counts.values())

def information_gain(rows, attribute):
    parent = entropy([label for _, label in rows])
    groups = defaultdict(list)
    for features, label in rows:
        groups[features[attribute]].append(label)
    weighted = sum((len(labels) / len(rows)) * entropy(labels)
                   for labels in groups.values())
    return parent - weighted

def build_tree(rows, attributes):
    labels = [label for _, label in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if not attributes:
        return Counter(labels).most_common(1)[0][0]
    best = max(attributes, key=lambda a: information_gain(rows, a))
    tree = {best: {}}
    values = set(features[best] for features, _ in rows)
    for value in values:
        subset = [row for row in rows if row[0][best] == value]
        remaining = [a for a in attributes if a != best]
        tree[best][value] = build_tree(subset, remaining)
    return tree

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = sample.get(attribute)
    branch = tree[attribute].get(value)
    if branch is None:
        return "Unknown"
    return predict(branch, sample)

if __name__ == "__main__":
    tree = build_tree(data, ["Outlook", "Wind"])
    print("Decision tree:", tree)
    test = {"Outlook": "Rain", "Wind": "Weak"}
    print("Test sample:", test)
    print("Prediction:", predict(tree, test))
