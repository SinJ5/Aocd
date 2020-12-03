from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=1)

data = puzzle.input_data.split("\n")
print(data)
result =0
for i in data:
    for j in data:

        if (int(i)+int(j)) ==2020:
            result = int(i)*int(j)

print("2020-Day1-A result: ", result)

puzzle.answer_a = result