from aocd.models import Puzzle
from itertools import permutations
from int_code_computer import IntCodeComputer

puzzle = Puzzle(year=2019, day=7)


prog=[ int(x)  for x in puzzle.input_data.split(",") ]

phase= permutations([0,1,2,3,4],5)

comp = IntCodeComputer(prog)

bestPh=None
maximumTrust=0;
for ph in phase:
    out=0
    inp=0
    for part in ph:
        comp.reset()
        out =comp.parseCode([part,inp])
        inp=out;
    if out>maximumTrust:
        maximumTrust=out
        bestPh=ph
        print(maximumTrust, "=>",ph)


puzzle.answer_a=maximumTrust





