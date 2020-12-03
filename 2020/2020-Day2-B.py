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
    s= tmp1[1]
    c=tmp2[1]
    if (s[int(tmpnum[0])]==c and s[int(tmpnum[1])]!=c) or(s[int(tmpnum[0])]!=c and s[int(tmpnum[1])]==c):
        result=result+1




print("2020-Day2-B result: ", result)

puzzle.answer_b = result