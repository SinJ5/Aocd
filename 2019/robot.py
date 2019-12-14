from int_code_computer2 import IntCodeComputer2, STATUS_END_OF_PROGRAM, STATUS_STOP_ON_OUTPUT, STATUS_NEED_INPUT

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

BLACK = 0
WHITE = 1


class Robot:
    def __init__(self, code,default=BLACK):
        self.brain = IntCodeComputer2(code, True,False,False)
        self.direction = UP
        self.position = [0, 0]
        if default==BLACK:
            self.map = {"0,0": 0}
        else:
            self.map = {"0,0": 1}
        self.mem=set([])
        self.defVal=default
        self.paintCount = 0


    def turn(self, val):
        if val == 0:  # turn left
            self.direction = (self.direction + 3) % 4
        else:  # turn right
            self.direction = (self.direction + 1) % 4

    def move(self):
        if (self.direction == UP):
            self.position[1] += 1
        elif (self.direction == DOWN):
            self.position[1] -= 1
        elif (self.direction == RIGHT):
            self.position[0] += 1
        elif (self.direction == LEFT):
            self.position[0] -= 1
        else:
            raise Exception("wrong direction")

    def posistionTag(self):
        return str(self.position[0]) + "," + str(self.position[1])

    def sensors(self):
        key = self.posistionTag()
        if self.map.get(key) != None:
            return self.map.get(key)
        self.map[key] = self.defVal
        return self.defVal

    def paint(self, val):
        key = self.posistionTag()
        if (val == BLACK and self.sensors() == WHITE):
            self.map[key] = BLACK
            if  not (key in self.mem):
                self.mem.add(key)
                self.paintCount += 1
        elif (val == WHITE and self.sensors() == BLACK):
            self.map[key] = WHITE
            if  not (key in self.mem):
                self.mem.add(key)
                self.paintCount += 1

    def run(self):
        self.brain.reset()
        self.brain.addInput(0)
        output = []

        while self.brain.run() != STATUS_END_OF_PROGRAM:
            if (self.brain.status == STATUS_STOP_ON_OUTPUT):
                output.append(self.brain.output)
                if (len(output) == 2):
                    self.paint(output[0])
                    self.turn(output[1])
                    self.move()
                    output = []
                    self.brain.addInput(self.sensors())

            if (self.brain.status == STATUS_NEED_INPUT):
                self.brain.addInput(self.sensors())
