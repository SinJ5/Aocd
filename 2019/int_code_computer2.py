STATUS_READY = 0
STATUS_RUN = 5
STATUS_NEED_INPUT = 10
STATUS_STOP_ON_OUTPUT = 20
STATUS_END_OF_PROGRAM = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


class IntCodeComputer2:

    def __init__(self, code, stopOnOutput=False, debug=False,printOutput = True):
        self.code = code.copy()
        self.program = code.copy()
        self.stopOnOutput = stopOnOutput
        self.status = STATUS_READY
        self.printOutput=printOutput
        if debug:
            self.debug = print
        else:
            self.debug = self.no_print
        self.step = 0
        self.output = None
        self.inputs = []
        self.relativeBase = 0
        self.cmd = {1: self.sum,
                    2: self.mult,
                    3: self.input,
                    4: self.out,
                    5: self.if_true,
                    6: self.if_false,
                    7: self.if_less,
                    8: self.if_equal,
                    9: self.changeBase,
                    99: self.end
                    }

    def reset(self):
        self.debug("reset")
        self.program = self.code.copy()
        self.step = 0
        self.status = STATUS_READY
        self.inputs = []
        self.relativeBase = 0

    def no_print(self, *allargs):
        return

    def addStep(self):
        self.debug("add step")
        self.step += 1

    def stepBack(self):
        self.debug("stepBack")
        self.step -= 1

    def addInput(self, val):
        self.debug("add input value=", val)
        self.inputs.append(val)

    def addInputAll(self, val):
        self.debug("add inputAll value=", val)
        self.inputs=val

    def get_arg_mode(self, op, i):
        tmp = str(op).rjust(5, "0")
        self.debug("get_arg_mode op:", op, " i:", i, " =", int(tmp[-3 - i]))
        return int(tmp[-3 - i])

    def getValue(self, op, index):
        arg_mode = self.get_arg_mode(op, index)
        if arg_mode == POSITION_MODE:
            out = self.program[self.program[self.step]]
        elif arg_mode == IMMEDIATE_MODE:
            out = self.program[self.step]
        elif arg_mode == RELATIVE_MODE:
            out = self.program[self.relativeBase + self.program[self.step]]
        else:
            raise Exception("Invalid arg mode: ", arg_mode)
        self.debug("getvalue step=", self.step, " arg_mode:", arg_mode, " out=", out)
        self.addStep()
        return out

    def setValue(self, op, index, val):
        arg_mode = self.get_arg_mode(op, index)
        self.debug("getvalue step=", self.step, " arg_mode:", arg_mode, " val=", val)
        if arg_mode == POSITION_MODE:
            self.program[self.program[self.step]] = val
        elif arg_mode == IMMEDIATE_MODE:
            self.program[self.step] = val
        elif arg_mode == RELATIVE_MODE:
            self.program[self.relativeBase + self.program[self.step]] = val
        else:
            raise Exception("Invalid arg mode: ", arg_mode)
        self.addStep()

    def mult(self, op):
        self.debug("op multiplication")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        self.setValue(op, 2, input_a * input_b)

    def sum(self, op):
        self.debug("op sum")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        self.setValue(op, 2, input_a + input_b)

    def input(self, op):
        self.debug("op input")
        if len(self.inputs) == 0:
            self.status = STATUS_NEED_INPUT
            self.stepBack()
            return self.status
        self.setValue(op, 0, self.inputs.pop(0))

    def out(self, op):
        self.debug("op output")
        input_a = self.getValue(op, 0)
        self.output = input_a
        if self.printOutput:
            print(self.output)
        if self.stopOnOutput:
            self.status = STATUS_STOP_ON_OUTPUT
            return

    def if_true(self, op):
        self.debug("op true")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        if input_a != 0:
            self.step = input_b
        self.debug("op true step=", self.step)

    def if_false(self, op):
        self.debug("op false")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        if input_a == 0:
            self.step = input_b
        self.debug("op false step=", self.step)

    def if_less(self, op):
        self.debug("op less")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        if input_a < input_b:
            self.setValue(op, 2, 1)
        else:
            self.setValue(op, 2, 0)

    def if_equal(self, op):
        self.debug("op equal")
        input_a = self.getValue(op, 0)
        input_b = self.getValue(op, 1)
        if input_a == input_b:
            self.setValue(op, 2, 1)
        else:
            self.setValue(op, 2, 0)

    def end(self, op):
        self.debug("op end")
        self.step -= 1
        self.status = STATUS_END_OF_PROGRAM

    def getNextOp(self):

        out = self.program[self.step]
        self.addStep()
        self.debug("get next OP =", out)
        return out

    def changeBase(self, op):
        self.debug("op change base")
        self.relativeBase += self.getValue(op, 0)
        self.debug("change base=", self.relativeBase)

    def run(self):
        self.status = STATUS_RUN
        while self.status == STATUS_RUN:
            op = self.getNextOp()
            self.cmd[op % 100](op)

        return self.status
