from aocd.models import Puzzle


puzzle = Puzzle(year=2019, day=3)

AllVal=puzzle.input_data.split("\n")



def createLine(x,y,val):
    ''' vytvopri tuple , ktery obhsahuje pocatecni souradnice usecky a konecne souradnice usecky a delku'''
    x0=x
    y0=y
    cmd=val[0]
    index=int(val[1:])
    if (cmd=="U"):
        x1=x0
        y1=y0+index
    if (cmd == "R"):
        x1 = x0 + index
        y1 = y0
    if (cmd == "L"):
        x1 = x0 - index
        y1 = y0
    if (cmd == "D"):
        x1 = x0
        y1 = y0 - index
    return (x0,y0,x1,y1,index)

def createAllLinesForOneWire( inp):
    ''' vrati list vsech primek pro  jeden drat'''
    tmpLines= inp.split(",")
    x=0
    y=0
    out=[]
    for each in tmpLines:
        tmp=createLine(x,y,each)
        x=tmp[2]
        y=tmp[3]
        out.append(tmp)
    return out

def isIn(val, A ,B):
    ''' je val v rozsahu A-B nebo B-A'''
    if(A>val and B<val):
        return True
    if (A < val and B > val):
        return True
    return False

def isCrosed(lineA,lineB):
    ''' zjistuje zda se primky protinaji   vraci vzdalenost  '''
    if((lineA[0]-lineA[2]!=0 and  lineB[0]-lineB[2]!=0) or(lineA[1]-lineA[3]!=0 and  lineB[1]-lineB[3]!=0) ):
        return 99999999  # linky jsou rovnobezne

    if(lineA[0]==lineA[2] and isIn(lineA[0],lineB[0],lineB[2])and isIn(lineB[1],lineA[1],lineA[3])):
        return abs(lineA[0])+abs(lineB[1])

    if (lineA[1] == lineA[3] and isIn(lineA[1], lineB[1], lineB[3]) and isIn(lineB[0], lineA[0], lineA[2])):
        return abs(lineA[1]) + abs(lineB[0])
    return 99999999


LinesA=createAllLinesForOneWire(AllVal[0])
LinesB = createAllLinesForOneWire(AllVal[1])
result= 99999999
for la in LinesA:
    for lb in LinesB:
        tmp = isCrosed(la,lb)
        if(tmp<result):
            result=tmp


print("2019-Day2-A result:",result)
puzzle.answer_a=result

