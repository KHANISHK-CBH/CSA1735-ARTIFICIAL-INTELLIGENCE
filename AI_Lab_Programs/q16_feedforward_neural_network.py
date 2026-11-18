# Q16. Feed Forward Neural Network (one hidden layer, NumPy not required)
# Trains a tiny network on the XOR truth table using sigmoid activation.

import math
import random

random.seed(1)

def sigmoid(x):
    x = max(-60, min(60, x))
    return 1 / (1 + math.exp(-x))

def dsigmoid(y):
    return y * (1 - y)

def dot(weights, inputs, bias):
    return sum(w * x for w, x in zip(weights, inputs)) + bias

# XOR dataset
training = [([0, 0], [0]), ([0, 1], [1]),
            ([1, 0], [1]), ([1, 1], [0])]

# 2 input nodes -> 2 hidden nodes -> 1 output node
w_hidden = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
b_hidden = [0.0, 0.0]
w_output = [random.uniform(-1, 1) for _ in range(2)]
b_output = 0.0
learning_rate = 0.7

for epoch in range(20000):
    for inputs, target in training:
        hidden = [sigmoid(dot(w_hidden[j], inputs, b_hidden[j]))
                  for j in range(2)]
        output = sigmoid(dot(w_output, hidden, b_output))

        output_error = target[0] - output
        output_delta = output_error * dsigmoid(output)

        hidden_deltas = []
        for j in range(2):
            hidden_error = output_delta * w_output[j]
            hidden_deltas.append(hidden_error * dsigmoid(hidden[j]))

        for j in range(2):
            w_output[j] += learning_rate * output_delta * hidden[j]
        b_output += learning_rate * output_delta

        for j in range(2):
            for k in range(2):
                w_hidden[j][k] += learning_rate * hidden_deltas[j] * inputs[k]
            b_hidden[j] += learning_rate * hidden_deltas[j]

print("XOR predictions:")
for inputs, target in training:
    hidden = [sigmoid(dot(w_hidden[j], inputs, b_hidden[j])) for j in range(2)]
    output = sigmoid(dot(w_output, hidden, b_output))
    print(f"{inputs} -> {output:.4f} (expected {target[0]})")
