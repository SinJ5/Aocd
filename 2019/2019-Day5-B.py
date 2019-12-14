from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2
puzzle = Puzzle(year=2019, day=5)




prog=[ int(x)  for x in puzzle.input_data.split(",") ]


comp =IntCodeComputer2(prog)
comp.addInput(5)
ret =comp.run()
print(ret)
result =comp.output

print("2019-Day5-B result:", result)
puzzle.answer_b=result
