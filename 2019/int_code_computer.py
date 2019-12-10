class IntCodeComputer:

    def __init__(self, code):
        self.code = code.copy()
        self.prog = code.copy()
        self.step = 0
        self.input_index = 0
        self.output = 0
        self.inputs = []
        self.stop = False
        self.reachEndofCode=False
        self.cmd = {1: self.sum,
                    2: self.mult,
                    3: self.input,
                    4: self.out,
                    5: self.if_true,
                    6: self.if_false,
                    7: self.if_less,
                    8: self.if_equal,
                    99: self.end
                    }

    def addstep(self):
        self.step += 1

    def reset(self):
        self.prog = self.code.copy()
        self.step=0
        self.inputs=[]
        self.input_index=0
        self.reachEndofCode = False




    def getValue(self, position_type):
        if position_type == 0:
            out = self.prog[self.prog[self.step]]
        else:
            out = self.prog[self.step]
        self.addstep()
        return out

    def mult(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        self.prog[self.prog[self.step]] = valA * valB
        self.addstep()

    def sum(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        self.prog[self.prog[self.step]] = valA + valB
        self.addstep()

    def input(self, op):
        if(self.input_index>=len(self.inputs)):
            self.stop=True
            self.step-=1
            return
        self.prog[self.prog[self.step]] = self.inputs[self.input_index]
        self.addstep()
        self.input_index+=1

    def out(self, op):
        self.output = self.prog[self.prog[self.step]]
        self.addstep()


    def if_true(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        if valA != 0:
            self.step = valB

    def if_false(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        if valA == 0:
            self.step = valB

    def if_less(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        if (valA < valB):
            self.prog[self.prog[self.step]] = 1
        else:
            self.prog[self.prog[self.step]] = 0
        self.addstep()

    def if_equal(self, op):
        valA = self.getValue((op // 100) % 10)
        valB = self.getValue((op // 1000) % 10)
        if (valA == valB):
            self.prog[self.prog[self.step]] = 1
        else:
            self.prog[self.prog[self.step]] = 0
        self.addstep()

    def end(self,op):
        self.stop=True
        self.reachEndofCode=True
        self.step-=1

    def getNext(self):
        out = self.prog[self.step]
        self.addstep()
        return out

    def parseCode(self, inputs=[0],resetStep=True,appendInput=False):
        if(appendInput):
            self.inputs+=inputs
        else:
            self.inputs=inputs
            self.input_index = 0
        if resetStep:
            self.step=0
        self.stop=False

        while not self.stop:
            op =self.getNext()
            self.cmd[op%100](op)

        return self.output


