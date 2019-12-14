from aocd.models import Puzzle
from itertools import permutations
from int_code_computer2 import IntCodeComputer2

puzzle = Puzzle(year=2019, day=7)


prog=[ int(x)  for x in puzzle.input_data.split(",") ]



comp = IntCodeComputer2(prog)
comp.reset()
comp.addInput(0)
bestPh=None
maximumTrust=0;
for ph in permutations([0,1,2,3,4],5):
    inp=0
    out=0
    for part in ph:
        comp.reset()
        comp.addInput(part)
        comp.addInput(inp)
        ret=comp.run()
        out=comp.output
        inp=out;
    if out>maximumTrust:
        maximumTrust=out
        bestPh=ph


print("2019-Day5-A result:", maximumTrust)
puzzle.answer_a=maximumTrust





