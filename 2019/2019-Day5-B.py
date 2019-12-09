from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=5)



# jo dal jsem to  :-)
prog=[ int(x)  for x in puzzle.input_data.split(",") ]



print ("result:",output)
puzzle.answer_b=output


inp =5
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
        continue

    if op % 10 == 2:  # mul
        valA = getVal(type0,step)
        step += 1
        valB = getVal(type1,step)
        step += 1
        prog[prog[step]] = valA * valB
        step += 1
        continue
    if op % 10 == 3:  # input
        prog[prog[step]]=inp
        step+=1
        continue
    if op % 10 == 4:  # output
        output=prog[prog[step]]
        step+=1
        continue
    if op % 10 == 5:  # jump if true
        valA = getVal(type0, step)
        step += 1
        valB = getVal(type1, step)
        step += 1
        if (valA != 0):
            step = valB
        continue
    if op % 10 == 6:  # jump if false
        valA = getVal(type0, step)
        step += 1
        valB = getVal(type1, step)
        step += 1
        if (valA == 0):
            step = valB
        continue
    if op % 10 == 7:  # less then
        valA = getVal(type0, step)
        step += 1
        valB = getVal(type1, step)
        step += 1
        if(valA<valB):
            prog[prog[step]] = 1
        else:
            prog[prog[step]] = 0
        step += 1
        continue
    if op % 10 == 8:  # equal
        valA = getVal(type0, step)
        step += 1
        valB = getVal(type1, step)
        step += 1
        if (valA == valB):
            prog[prog[step]] = 1
        else:
            prog[prog[step]] = 0
        step += 1
        continue
    print("necodivneho")
    break
