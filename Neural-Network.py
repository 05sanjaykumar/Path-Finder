import numpy as np
# Inputs (XOR truth table)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Outputs (XOR results)
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

np.random.seed(42)

# Weights for input -> hidden (2 inputs × 2 hidden neurons)
W1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))

# Weights for hidden -> output (2 hidden × 1 output neuron)
W2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x) 

# Forward pass
def forward(X, W1, b1, W2, b2):
    z1 = np.dot(X, W1) + b1      # Input to hidden layer
    a1 = sigmoid(z1)             # Activation of hidden layer
    z2 = np.dot(a1, W2) + b2     # Hidden to output layer
    a2 = sigmoid(z2)             # Final prediction (output layer)
    return a1, a2

# a1, a2 = forward(X, W1, b1, W2, b2)
# print("Predictions:\n", a1)


class NeuralNetwork:
    def __init__(self):
        self.input_size = 2
        self.hidden_size = 2
        self.output_size = 1

        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def predict(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        output = sigmoid(self.z2)
        return output
    
