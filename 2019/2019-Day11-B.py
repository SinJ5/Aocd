from aocd.models import Puzzle
from robot import Robot,WHITE

puzzle = Puzzle(year=2019, day=11)

data = puzzle.input_data.split("\n")

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]

rur=Robot(prog,WHITE)
rur.run()
minX=0
maxX=0
minY=0
maxY=0
for key,val in rur.map.items():
    tmp= [int(x) for x in  key.split(",")]
    if(minX>tmp[0]):
        minX=tmp[0]
    if(maxX<tmp[0]):
        maxX=tmp[0]
    if (minY > tmp[1]):
        minY = tmp[1]
    if (maxY < tmp[1]):
        maxY = tmp[1]
print(minX,minY,maxX,maxY)
flag = [[" "for x in range(maxX-minX+2)] for y in range(maxY-minY+2)]
for key,val in rur.map.items():
    tmp= [int(x) for x in  key.split(",")]
    x=tmp[0]-minX
    y=tmp[1]-minY
    if val==WHITE:
        flag[y][x]='#'
for t in flag:
    print("".join(t))
result="PCKRLPUK"
print("2019-Day11-B result:", result)
puzzle.answer_b = result
