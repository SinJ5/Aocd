from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT

puzzle = Puzzle(year=2019, day=15)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]
comp = IntCodeComputer2(prog,True,False,False)

comp.reset()

output = []
map ={}

NORTH ="1"
SOUTH ="2"
EAST ="4"
WEST ="3"

WALL=0
STEP=1
OXYGEN=2

trylist=[NORTH,EAST,WEST,SOUTH]
result=None
while len(trylist)>0:   
    run=trylist.pop(0)
    if result is not  None:        
        if(len(run)>result+1):
            break 
    #jj mam neomezene robotu tak nac se vracet :-)
    comp.reset() 
    index=0
    while comp.run() != STATUS_END_OF_PROGRAM:
        if (comp.status == STATUS_STOP_ON_OUTPUT):
            if(comp.output==WALL):
                break
            if(comp.output==OXYGEN):
                if(result is None or result>index):
                    result=index                                                
                break                            
        if comp.status == STATUS_NEED_INPUT:
            if(index<len(run)):
                comp.addInput(int(run[index]))
                index+=1
            else:
                if run[index-1]!=NORTH:
                    trylist.append(run+SOUTH)
                if run[index-1]!=SOUTH:
                    trylist.append(run+NORTH)
                if run[index-1]!=EAST:
                    trylist.append(run+WEST)
                if run[index-1]!=WEST:
                    trylist.append(run+EAST)
                break




print("2019-Day15-A result:", result)

puzzle.answer_a = result
