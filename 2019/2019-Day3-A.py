def readFile():
    ''' nacte vstupni soubor '''
    f = open("Day3", "r")
    Text = f.readlines()
    f.close()
    return Text

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
    ''' zjistuje zda se primky protinaji   vraci '''
    if((lineA[0]-lineA[2]!=0 and  lineB[0]-lineB[2]!=0) or(lineA[1]-lineA[3]!=0 and  lineB[1]-lineB[3]!=0) ):
        return 99999999  # linky jsou rovnobezne

    if(lineA[0]==lineA[2] and isIn(lineA[0],lineB[0],lineB[2])and isIn(lineB[1],lineA[1],lineA[3])):
        return abs(lineA[0])+abs(lineB[1])

    if (lineA[1] == lineA[3] and isIn(lineA[1], lineB[1], lineB[3]) and isIn(lineB[0], lineA[0], lineA[2])):
        return abs(lineA[1]) + abs(lineB[0])
    return 99999999

def partA():
    AllVal=readFile()
    LinesA=createAllLinesForOneWire(AllVal[0])
    LinesB = createAllLinesForOneWire(AllVal[1])
    out= 99999999
    for la in LinesA:
        for lb in LinesB:
            tmp = isCrosed(la,lb)
            if(tmp<out):
                out=tmp
    return out

print("day3partA:",partA())


def partB():
    AllVal = readFile()
    LinesA = createAllLinesForOneWire(AllVal[0])
    LinesB = createAllLinesForOneWire(AllVal[1])
    out = 99999999
    tempA=0
    tempB=0
    for la in LinesA:
        tempB=0
        for lb in LinesB:
            tmp = isCrosed(la, lb)
            if (tmp !=99999999 ):
                tmp =(tempA + tempB)
                tmp +=abs(la[0]-lb[0])
                tmp += abs(la[1] - lb[1])
                if(tmp<out):
                    out=tmp
            tempB += lb[4]
        tempA += la[4]
    return out


print("day3partB:",partB())