from aocd.models import Puzzle
from itertools import permutations

puzzle = Puzzle(year=2019, day=7)


class ampl:
    def __init__(self,code):
        self.code=code
        self.prog=code

    def getVal(self,type):
        output=self.prog[self.prog[self.step]]
        if type == 1:
             output=self.prog[self.step]
        self.step+=1
        return output



    def parseCode(self,inputA,inputB):
        self.prog=self.code
        self.step=0
        input=inputA
        while self.prog[self.step] != 99:
            op = self.prog[self.step]
            self.step += 1
            type0 = (op // 100) % 10
            type1 = (op // 1000) % 10
            if op % 10 == 1:  # sum
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                self.prog[self.prog[self.step]] = valA + valB
                self.step += 1
                continue
            if op % 10 == 2:  # mul
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                self.prog[self.prog[self.step]] = valA * valB
                self.step += 1
                continue
            if op % 10 == 3:  # input
                self.prog[self.prog[self.step]] = input
                input=inputB
                self.step += 1
                continue
            if op % 10 == 4:  # output
                self.output = self.prog[self.prog[self.step]]
                self.step += 1
                continue
            if op % 10 == 5:  # jump if true
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                if (valA != 0):
                    self.step = valB
                continue
            if op % 10 == 6:  # jump if false
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                if (valA == 0):
                    self.step  = valB
                continue
            if op % 10 == 7:  # less then
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                if (valA < valB):
                    self.prog[self.prog[self.step]] = 1
                else:
                    self.prog[self.prog[self.step]] = 0
                self.step += 1
                continue
            if op % 10 == 8:  # equal
                valA = self.getVal(type0)
                valB = self.getVal(type1)
                if (valA == valB):
                    self.prog[self.prog[self.step]] = 1
                else:
                    self.prog[self.prog[self.step]] = 0
                self.step += 1
                continue
            print("necodivneho")
            break
        return self.output

phase= permutations([0,1,2,3,4],5)

ampl=ampl([ int(x)  for x in puzzle.input_data.split(",") ])
bestPh=None
maximumTrust=0;
for ph in phase:
    out=0
    inp=0

    for part in ph:
        out =ampl.parseCode(part,inp)
        inp=out;
    if out>maximumTrust:
        maximumTrust=out
        bestPh=ph
        print(maximumTrust, "=>",ph)


puzzle.answer_a=maximumTrust





