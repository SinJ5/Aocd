from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT

puzzle = Puzzle(year=2019, day=13)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]
prog[0]=2
comp = IntCodeComputer2(prog,True,False,False)

comp.reset()

BALL=4
PADDLE=3

output = []
map ={}
score=0;

def getKey(val):
    for pos ,title  in map.items():
        if title == val:
            return pos


while comp.run() != STATUS_END_OF_PROGRAM:
    if (comp.status == STATUS_STOP_ON_OUTPUT):
        output.append(comp.output)
        if (len(output) == 3):
            if(output[0]==-1 and output[1]==0):
                score=output[2]
                output = []
                continue            
            map[(output[0],output[1])]=output[2]
            output = []
                        
    if comp.status == STATUS_NEED_INPUT:
        ball = getKey(BALL)
        paddle= getKey(PADDLE)
        if ball[0]==paddle[0]:
            comp.addInput(0)
        if ball[0]>paddle[0]:
            comp.addInput(1)
        if ball[0]<paddle[0]:
            comp.addInput(-1)
        

print(map)

result=score


print("2019-Day13-B result:", result)

puzzle.answer_b = result
