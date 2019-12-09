from aocd.models import Puzzle
from int_code_computer import IntCodeComputer

puzzle = Puzzle(year=2019, day=2)
target = 19690720

prog = [int(x) for x in puzzle.input_data.split(",")]

comp = IntCodeComputer(prog)



def compute(n, v):
    comp.reset()
    comp.prog[1] = n
    comp.prog[2] = v
    comp.parseCode([])
    return comp.prog[0]


for noun in range(0, 99, 1):
    for verb in range(0, 99, 1):
        tmp = compute(noun, verb)
        if tmp == target:
            result = (noun * 100) + verb
            print("2019-Day2-B result:", result)
            puzzle.answer_b = result
            exit(0)
