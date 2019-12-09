from aocd.models import Puzzle
from int_code_computer import IntCodeComputer
puzzle = Puzzle(year=2019, day=5)




prog=[ int(x)  for x in puzzle.input_data.split(",") ]


comp =IntCodeComputer(prog)

result =comp.parseCode([1])


print("2019-Day5-A result:", result)
puzzle.answer_a=result


