from aocd.models import Puzzle
from ShowMap import ShowMap
puzzle = Puzzle(year=2019, day=8)

layer_width = 25
layer_height = 6
layer_len = layer_height * layer_width
data = [int(x) for x in puzzle.input_data]
layer_count = len(data) // layer_len
result_img = [2] * layer_len

for img_pos in range(0,layer_len):
    for layer in range(0,layer_count):
        index=img_pos+(layer*layer_len)
        pixel=data[index]
        if(pixel<2):
            result_img[img_pos]=pixel
            break
dmap =ShowMap({0:" ",1:"#"})
dmap.makeFrame({(pos%layer_width,pos//layer_width):val for pos,val in enumerate(result_img)})
dmap.draw()



print("2019-Day8-B result:", "GKCKH")
puzzle.answer_b = "GKCKH"