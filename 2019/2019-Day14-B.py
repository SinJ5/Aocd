from aocd.models import Puzzle
from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT
import math

puzzle = Puzzle(year=2019, day=14)

data =puzzle.input_data.split("\n")
rmap={}


class reaction:
    def __init__(self,inputs,output):
        self.key=output[1]
        self.amount=output[0]
        self.inputs=inputs    
        self.have=0
    
    def __str__(self):
        return self.key+ "="+ str(self.have)
        
        
def parsePair(pair):
    tmp =pair.strip().split(" ")
    return (int(tmp[0]),tmp[1])

def parseInputLine(line):
    line =line.strip()
    tmp = line.split("=>")
    out =  parsePair(tmp[1])     
    input = tuple([parsePair(x) for x in tmp[0].split(",")])            
    react= reaction(input,out)
    rmap[react.key]=react
 


for line in data:
    parseInputLine(line)




def makeReaction(ore,amount,name):
    if(name=="ORE"):
        ore+=amount
        need[name]-=amount
        if need[name]==0:
            del need[name]
        return ore
    react=rmap[name]
    if react is None:
        print("chyba neznama  reakce",name)
        exit()
    react.have-=amount
    
    if(react.have<0):
        cnt=math.ceil( abs(react.have)/react.amount)        
        while react.have<0:
            for inp in react.inputs:
                if inp[1] in need:
                    need[inp[1]]+=inp[0]*cnt                               
                else:
                    need[inp[1]]=inp[0]*cnt
            react.have+=react.amount*cnt
    
    need[name]-=amount
    if need[name]==0:
        del need[name]
    return ore
MAX_ORE=1000000000000
maxOre =MAX_ORE
result=0

while maxOre>0:
    ore=0
    cnt=maxOre//int(puzzle.answer_a)
    need = {"FUEL":cnt}
    result+=cnt    
    while len(need)>0:
        if(ore>maxOre):
            maxOre=0
            result-=cnt
            break;            
        needTmp =need.copy()
        for name,val in needTmp.items():
                ore=makeReaction(ore,val, name)

    maxOre-=ore
    if(maxOre<int(puzzle.answer_a)):
        break
    #print("result:",result, " cnt:",cnt," maxOre",maxOre)     



print("2019-Day14-B result:", result)

puzzle.answer_b = result
