from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2,STATUS_END_OF_PROGRAM

puzzle = Puzzle(year=2019, day=9)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]
comp = IntCodeComputer2(prog,False,False,False)
comp.reset()
comp.addInput(2)
ret =comp.run()
if(ret== STATUS_END_OF_PROGRAM):
    result = comp.output


print("2019-Day9-B result:", result)
puzzle.answer_b=result



