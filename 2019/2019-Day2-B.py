from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2

puzzle = Puzzle(year=2019, day=2)
target = 19690720

prog = [int(x) for x in puzzle.input_data.split(",")]

comp = IntCodeComputer2(prog)



def compute(n, v):
    comp.reset()
    comp.program[1] = n
    comp.program[2] = v
    comp.run()
    return comp.program[0]


for noun in range(0, 99, 1):
    for verb in range(0, 99, 1):
        tmp = compute(noun, verb)
        if tmp == target:
            result = (noun * 100) + verb
            print("2019-Day2-B result:", result)
            puzzle.answer_b = result
            exit(0)

