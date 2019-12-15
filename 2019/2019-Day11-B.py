from aocd.models import Puzzle
from robot import Robot,WHITE,BLACK
from ShowMap import ShowMap
puzzle = Puzzle(year=2019, day=11)

data = puzzle.input_data.split("\n")

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]

rur=Robot(prog,WHITE)
rur.run()

dmap =ShowMap({BLACK:" ",WHITE:"#"})
dmap.makeFrame(rur.map)
dmap.draw()


result="PCKRLPUK"
print("2019-Day11-B result:", result)
puzzle.answer_b = result
