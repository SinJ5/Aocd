from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=1)

data = puzzle.input_data.split("\n")
print(data)
data= [int(d) for d in data]
result =0
for i in data:
    for j in data:
        for k in data:
            if (i+j+k) ==2020:
                result = i*j*k

print("2020-Day2-A result: ", result)

puzzle.answer_b = result