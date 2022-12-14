import numpy as np
# Zabrina Rulif Aurellia
# 21091397056 - 2021B
inputs = [
    [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
    [1.6, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 4.4, 4.8, 5.2],
    [3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2],
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 1.2],
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    [0.8, 0.10, 0.13, 0.14, 0.50, 0.6, 0.7, 0.18, 0.9, 1.0],
]

weights1 = [
    [0.2, 0.1, 0.5, 0.8, 0.7, 0.6, 0.3, 0.9, 1.1, 1.3],
    [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0],
    [1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1],
    [2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 4.3, 4.9],
    [7.7, 7.9, 8.1, 8.3, 8.5, 8.7, 8.9, 9.1, 9.3, 9.5]
]

biases1 = [0.4, 1.3, 2.6, 3.2, 4.6]

weights2 = [
    [5.0, 3.5, 2.0, 5.1, 5.7],
    [2.5, 3.1, 2.2, 1.8, 3.2],
    [6.2, 1.8, 2.9, 1.2, 2.6]
]

biases2 = [2.0, 7.2, 2.1]

w = np.dot(inputs, np.array(weights1) . T)
outputs1 = np.dot(inputs, np.array(weights1) . T) + biases1
outputs2 = np.dot(outputs1, np.array(weights2) . T) + biases2
print(outputs1)