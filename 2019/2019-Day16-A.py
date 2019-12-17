from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT

puzzle = Puzzle(year=2019, day=16)
data =[int(x)   for x in  puzzle.input_data ]
#data=[1,2,3,4,5,6,7,8]

delkaDat=len(data) 
print (data)

def generateSin(period,length):
    tmp =[0]*period
    tmp += [1]*period
    tmp += [0]*period
    tmp += [-1]*period    
    out =tmp;
    while len(out)<length:
        out+=tmp    
    return out

inputData=data
sinTab={}
for i in range(1,delkaDat+2):
    sinTab[i]=generateSin(i,delkaDat+2)

for cnt in range(100):
    print("cnt",cnt)
    newdata=[0]*delkaDat
    for i in range(0,delkaDat):
        newdata[i]= abs(sum([ dato*sinTab[i+1][j+1]   for j,dato in enumerate(inputData)  ]))%10    
    inputData=newdata


result ="".join([str(x) for x in  inputData[0:8]])

print("2019-Day16-A result:", result)

puzzle.answer_a = result
