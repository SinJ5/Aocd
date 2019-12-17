from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT
from ShowMap import ShowMap
from VacuumRobot import pathFinderForVacuumRobot
puzzle = Puzzle(year=2019, day=17)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]

SCAFOLD=35
VACUUM=46
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

vc= pathFinderForVacuumRobot(rmap)
path= ",".join([str(x) for x in vc.pathFinder()[1:]])
dmap.makeFrame(vc.maps)
dmap.draw()
print(path)
a= "R,6,L,8,R,8"
b= "R,4,R,6,R,6,R,4,R,4"
c= "L,8,R,6,L,10,L,10"
print("A=",a,"  len:",len(a))
print("B=",b,"  len:",len(b))
print("C=",c,"  len:",len(c))
path = path.replace(a, "A")
path = path.replace(b, "B")
path = path.replace(c, "C")
print("main=",path, " len:",len(path))
mainAscii=[ord(x) for x in path]+[10]
aAscii=[ord(x) for x in a]+[10]
bAscii=[ord(x) for x in b]+[10]
cAscii=[ord(x) for x in c]+[10]

inputs=mainAscii+aAscii+bAscii+cAscii+[ord("n"),10]
comp2 = IntCodeComputer2(prog,False,False,False)
comp2.reset() 
comp2.program[0]=2
comp2.addInputAll(inputs)
while comp2.run() != STATUS_END_OF_PROGRAM:
    if (comp2.status == STATUS_STOP_ON_OUTPUT):
         result=comp2.output
         break;
    if (comp2.status == STATUS_NEED_INPUT): 
         exit()
result=comp2.output         
print("2019-Day17-B result:", result)

puzzle.answer_b = result
