from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2019, day=10)

data = puzzle.input_data.split("\n")


meteorlist = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            meteorlist.append((x, y))

best=(17,22)

def distance(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))

meteror_map=[ ((((math.atan2(best[0]-tmp[0],tmp[1]-best[1])/math.pi)*180)+180)%360 ,distance(best,tmp),tmp[0],tmp[1]) for tmp in meteorlist if tmp!=best]

meteror_map.sort()
count=0
result=None
while  len(meteror_map)>0:
    lastAngle=None
    for target in meteror_map.copy():
        if(target[0]==lastAngle):
            continue
        meteror_map.remove(target)
        count+=1
        lastAngle=target[0]
        if(count==200):
            result=(target[2]*100)+target[3]
            break;
    if result is not  None:
        break;


print("2019-Day10-B result:", result)
puzzle.answer_b = result
