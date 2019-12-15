from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT
from ShowMap import ShowMap

puzzle = Puzzle(year=2019, day=15)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]
comp = IntCodeComputer2(prog,True,False,False)

comp.reset()

output = []



NORTH ="1"
SOUTH ="2"
EAST ="4"
WEST ="3"

WALL=0
STEP=1
OXYGEN=2
START =4
rmap ={(0,0):4}
LEGEND={WALL:"#",OXYGEN:"o",STEP:".",START:"^"}


def getKey(sequence):
    return (sequence.count(WEST)-sequence.count(EAST),sequence.count(NORTH)-sequence.count(SOUTH))
     

trylist=[NORTH,EAST,WEST,SOUTH]
result=None
while len(trylist)>0:   
    run=trylist.pop(0)
    key=getKey(run)
    if key in rmap:
        continue
    comp.reset() 
    index=0
    path=""
    lastOutput=None
    while comp.run() != STATUS_END_OF_PROGRAM:
        if (comp.status == STATUS_STOP_ON_OUTPUT):
            lastOutput=comp.output
            if(comp.output==WALL):
                rmap[getKey(path)]=WALL              
                break                                    
        if comp.status == STATUS_NEED_INPUT:
            if(index<len(run)):
                comp.addInput(int(run[index]))
                path+=run[index]
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
                rmap[getKey(path)]=lastOutput
                break
print(rmap)                    
dmap =ShowMap(LEGEND)
dmap.makeFrame(rmap)
dmap.draw()   

vacuumList=[ pos for pos,val in rmap.items() if val==STEP or val==START]

time=0
while len(vacuumList)>0:
    tmpMap=rmap.copy()
    vacuumListTmp=vacuumList.copy()
    for pos in vacuumListTmp:
        if tmpMap[(pos[0]+1,pos[1])]==OXYGEN: 
            vacuumList.remove(pos)
            rmap[pos]=OXYGEN
            continue
        if tmpMap[(pos[0]-1,pos[1])]==OXYGEN: 
            vacuumList.remove(pos)
            rmap[pos]=OXYGEN
            continue
        if tmpMap[(pos[0],pos[1]+1)]==OXYGEN: 
            vacuumList.remove(pos)
            rmap[pos]=OXYGEN
            continue
        if tmpMap[(pos[0],pos[1]-1)]==OXYGEN: 
            vacuumList.remove(pos)
            rmap[pos]=OXYGEN
            continue
    time+=1
print("\n")
print("=======================================================================")
print("time:",time)          
dmap.makeFrame(rmap)
dmap.draw()  
print("=======================================================================")

result =time


print("2019-Day15-B result:", result)

puzzle.answer_b = result
