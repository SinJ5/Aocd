from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)

data = puzzle.input_data.split("\n")

print(data)

result=0
cnt=[0,0,0,0,0]
for i,d in enumerate(data):
    if d[(i)%len(d)]=='#':
        cnt[0]=cnt[0]+1
    if d[(i*3)%len(d)]=='#':
        cnt[1]=cnt[1]+1
    if d[(i*5)%len(d)]=='#':
        cnt[2]=cnt[2]+1
    if d[(i*7) % len(d)] == '#':
        cnt[3] = cnt[3] + 1
    if (i%2)==0 and d[(int(i/2)) % len(d)] == '#':
        cnt[4] = cnt[4] + 1

result= cnt[0]*cnt[1]*cnt[2]*cnt[3]*cnt[4]

print("2020-Day3-B result: ", result)

puzzle.answer_b = result

