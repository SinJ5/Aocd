from aocd.models import Puzzle
from int_code_computer import IntCodeComputer

puzzle = Puzzle(year=2019, day=2)

prog = [int(x) for x in puzzle.input_data.split(",")]

prog[1] = 12
prog[2] = 2
comp = IntCodeComputer(prog)

comp.parseCode([])
result = comp.prog[0]

print("2019-Day2-A result:", result)
puzzle.answer_a = result
