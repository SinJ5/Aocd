from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=5)

print(puzzle.input_data)


prog=[ int(x)  for x in puzzle.input_data.split(",") ]
print(prog)

inp =1
output=0
step = 0

def getVal(type,st):

    if type==1:
        return prog[st]
    return prog[prog[st]]



while prog[step]!=99:
    op =prog[step]
    step+=1
    type0=(op//100)%10
    type1 = (op // 1000) % 10
    if op%10 ==1:#sum
        valA=getVal(type0,step)
        step+=1
        valB=getVal(type1,step)
        step += 1
        prog[prog[step]]=valA+valB
        step += 1

    if op % 10 == 2:  # mul
        valA = getVal(type0,step)
        step += 1
        valB = getVal(type1,step)
        step += 1
        prog[prog[step]] = valA * valB
        step += 1
    if op % 10 == 3:  # input
        prog[prog[step]]=inp
        step+=1
    if op % 10 == 4:  # output
        output=prog[prog[step]]
        step+=1

print (output)
puzzle.answer_a=output


