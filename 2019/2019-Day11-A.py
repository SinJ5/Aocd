from aocd.models import Puzzle
from robot import Robot

puzzle = Puzzle(year=2019, day=11)

data = puzzle.input_data.split("\n")
result =0

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]

rur=Robot(prog)
rur.run()
result=rur.paintCount
print("2019-Day11-A result:", result)
puzzle.answer_a = result
