from aocd.models import Puzzle
from itertools import permutations
from int_code_computer2 import IntCodeComputer2,STATUS_END_OF_PROGRAM

puzzle = Puzzle(year=2019, day=7)


prog=[ int(x)  for x in puzzle.input_data.split(",") ]

phase_permutation = permutations([5, 6, 7, 8, 9], 5)






allampl = [IntCodeComputer2(prog,True,False,False) for x in range(0,5)]
print(allampl)

bestPh = None
maximumTrust = 0;
for phases in phase_permutation:
    out = 0
    inp = 0
    for i in range(0, 5):
        allampl[i].reset()
        allampl[i].addInput(phases[i])
    first=True
    while not allampl[0].status ==STATUS_END_OF_PROGRAM:
        for i in range(0, 5):
            allampl[i].addInput(inp)
            allampl[i].run()
            out=allampl[i].output
            inp = out
        first=False
    if out > maximumTrust:
        maximumTrust = out
        bestPh = phases
        print(maximumTrust, "=>", bestPh)
print("2019-Day7-B result:", maximumTrust)
19741286
puzzle.answer_b=maximumTrust
