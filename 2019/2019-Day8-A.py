from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=8)

layer_width = 25
layer_height = 6
layer_len = layer_height * layer_width
data = [int(x) for x in puzzle.input_data]
print(data)
layer_count = len(data) // layer_len
layers = []
count = 0
for pixel in data:
    layer_index = count // layer_len
    count += 1
    if ((len(layers) - 1) < layer_index):
        layers.append([0, 0, 0])
    layers[layer_index][pixel] += 1

tmp_result = [9999999, 0, 0]
for layer in layers:
    if (layer[0] < tmp_result[0]):
        tmp_result = layer

result = tmp_result[1] * tmp_result[2]
print("2019-Day8-A result:", result)
puzzle.answer_a = result
