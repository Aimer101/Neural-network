input = [1, 2, 3, 2.5]

weights = [
             [0.2, 0.8, -0.5, 1],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]
           ]

biases = [2, 3, 0.5]


layer_outputs = []

for bias_weight, bias in zip(weights, biases):
    temp = 0
    for input, weight in zip (inputs, bias_weight):
        temp += input * weight
    layer_outputs.append(temp + bias);

print(layer_outputs)



