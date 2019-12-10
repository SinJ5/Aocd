from aocd.models import Puzzle
from itertools import permutations
from int_code_computer import IntCodeComputer

puzzle = Puzzle(year=2019, day=7)


prog=[ int(x)  for x in puzzle.input_data.split(",") ]

#prog =[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase_permutation = permutations([5, 6, 7, 8, 9], 5)

#prog =[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]





allampl = [IntCodeComputer(prog) for x in range(0,5)]
print(allampl)

bestPh = None
maximumTrust = 0;
for phases in phase_permutation:
    out = 0
    inp = 0
    for i in range(0, 5):
        allampl[i].reset()
    first=True
    while not allampl[0].reachEndofCode:
    #for x in range(1,10):
        for i in range(0, 5):
            if first:
                inptArg=[phases[i],inp]
            else:
                inptArg = [inp]
            out = allampl[i].parseCode(inptArg,False,True)
            inp = out
        first=False
    if out > maximumTrust:
        maximumTrust = out
        bestPh = phases
        print(maximumTrust, "=>", bestPh)
print("2019-Day7-B result:", maximumTrust)
puzzle.answer_b=maximumTrust
