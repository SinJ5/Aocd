
def readFile ( ):
    ''' nacte vstupni soubor a prevede na list integeru'''
    f = open("day2", "r")
    Text = f.readlines()
    f.close()
    inputs = Text[0].split(",")
    out=[]
    for each in inputs:
        out.append(int (each))
    return out

def doOpt(prog,op ,indexA,indexB,indexOut):
    '''provede operaci  op nad daty z indexu A a B a vysledek ulozi do indexu Out '''
    valA=prog[indexA]
    valB=prog[indexB]
    if(op==1):
        prog[indexOut]=valA+valB
    if(op==2):
        prog[indexOut] = valA * valB


def partA( val1 ,val2):
    '''provede program se zadanym prametrm val1 a val2'''
    prog = readFile()
    actualIndex = 0
    prog[1] = val1
    prog[2] = val2
    while prog[actualIndex] != 99:
        doOpt(prog,prog[actualIndex], prog[actualIndex + 1], prog[actualIndex + 2], prog[actualIndex + 3])
        actualIndex += 4
    return prog[0]

print( "partA:",partA(12,2))

