from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT
from ShowMap import ShowMap
puzzle = Puzzle(year=2019, day=13)

prog=[ int(x)  for x in puzzle.input_data.split(",") ]+[0 for i in range(0,6000)]
comp = IntCodeComputer2(prog,True,False,False)

comp.reset()

output = []
map ={}

while comp.run() != STATUS_END_OF_PROGRAM:
    if (comp.status == STATUS_STOP_ON_OUTPUT):
        output.append(comp.output)
        if (len(output) == 3):
            map[(output[0],output[1])]=output[2]
            output = []            
            


dmap=ShowMap({0:".",1:"8",2:"#",3:"=",4:"*"})
dmap.makeFrame(map)
dmap.draw()

result=sum([1 for x in map.values() if x==2])


print("2019-Day13-A result:", result)

puzzle.answer_a = result
