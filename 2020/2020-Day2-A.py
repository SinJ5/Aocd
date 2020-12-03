from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=2)

data = puzzle.input_data.split("\n")
print(data)
result=0
for d in data:
    tmp1 = d.split(":")
    tmp2 = tmp1[0].split(" ")
    tmpnum=tmp2[0].split("-")
    pocet=0
    for c in tmp1[1]:
        if c==tmp2[1]:
            pocet=pocet+1
    if pocet >=int(tmpnum[0]) and pocet<=int(tmpnum[1]):
        result=result+1


print("2020-Day2-A result: ", result)

puzzle.answer_a = result