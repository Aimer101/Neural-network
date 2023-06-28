import numpy as np

np.random.seed(0)

X = [
        [1, 2, 3, 2.5],
        [2, 5, -1, 2.0],
        [-1.5, 2.7, 3.3, -0.8],
    ]

'''
################## TIPS ################
 TO INITIALIZE WEIGHT BETWEEN 0.1 AND -.01,
 TO INITIALIZE BIASES TO BE 0,
 BUT THERES A CASES WH ERE YOU DONT WANT TO DO THIS SINCE
 MULTIPLICATION OF 0 RESULTING IN 0 WHICH CAUSE THE NEURON TO BE DEAD NEURON
'''

class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        # multiply by 0.1 to make sure the value is within that bound
        self.weights = np.random.randn(n_inputs, n_neurons) * 0.1
        self.biases = np.zeros((1, n_neurons))


    def forward(self, inputs):
        self.outputs = np.dot(inputs, self.weights) + self.biases

layer1 = LayerDense(len(X[0]), 5)
layer2 = LayerDense(5, 2)

layer1.forward(X)
print(layer1.outputs)
layer2.forward(layer1.outputs)
print(layer2.outputs)