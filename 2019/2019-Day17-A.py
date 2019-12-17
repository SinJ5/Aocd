from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT
from ShowMap import ShowMap
puzzle = Puzzle(year=2019, day=17)
prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]

SCAFOLD=35
VACUUM=46
UP=94


NL=10

comp = IntCodeComputer2(prog,True,False,False)
comp.reset() 
index=0
rmap={}
x=0
y=0
while comp.run() != STATUS_END_OF_PROGRAM:
    if (comp.status == STATUS_STOP_ON_OUTPUT):     
        if(comp.output==NL):
            y+=1
            x=0
        else:            
            rmap[(x,y)]=comp.output
            x+=1

dmap =ShowMap(None)
dmap.makeFrame(rmap)
dmap.draw()   
result=0
for pos,data in rmap.items():
    if data==SCAFOLD and (pos[0]+1,pos[1])in rmap and rmap[(pos[0]+1,pos[1])]==SCAFOLD and (pos[0]-1,pos[1])in rmap and rmap[(pos[0]-1,pos[1])]==SCAFOLD and  (pos[0],pos[1]+1)in rmap and rmap[(pos[0],pos[1]+1)]==SCAFOLD and  (pos[0],pos[1]-1)in rmap and rmap[(pos[0],pos[1]-1)]==SCAFOLD:
        
        result+= pos[0]*pos[1]



print("2019-Day17-A result:", result)
puzzle.answer_a = result
