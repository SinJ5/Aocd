from aocd.models import Puzzle
from int_code_computer import IntCodeComputer

puzzle = Puzzle(year=2019, day=9)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,600)]
print(prog)
comp = IntCodeComputer(prog)
comp.reset()
result =comp.parseCode([1])

print("2019-Day9-A result:", result)
puzzle.answer_a=result



