from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2

puzzle = Puzzle(year=2019, day=2)

prog = [int(x) for x in puzzle.input_data.split(",")]

prog[1] = 12
prog[2] = 2
comp = IntCodeComputer2(prog)


comp.run()
result = comp.program[0]

print("2019-Day2-A result:", result)
puzzle.answer_a = result
