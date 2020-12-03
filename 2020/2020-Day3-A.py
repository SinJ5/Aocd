from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)

data = puzzle.input_data.split("\n")
print(len(data))
result=0

for i,d in enumerate(data):
    if d[(i*3)%len(d)]=='#':
        result=result+1


print("2020-Day3-A result: ", result)

puzzle.answer_a = result