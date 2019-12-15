from aocd.models import Puzzle
import numpy



puzzle = Puzzle(year=2019, day=12)

data = puzzle.input_data.split("\n")
print(data)



class Moon:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.startX=x
        self.startY=y
        self.startZ=z
        self.velX=0
        self.velY=0
        self.velZ = 0
        self.period=0

    def changePos(self):
        self.x+=self.velX
        self.y += self.velY
        self.z += self.velZ

    def changeVel(self,moons):
        for mn in moons:
            if self==mn:
                continue            
            if(self.x>mn.x):
                self.velX-=1
            elif(self.x<mn.x):
                self.velX+=1
            if(self.y>mn.y):
                self.velY-=1
            elif(self.y<mn.y):
                self.velY+=1
            if(self.z>mn.z):
                self.velZ-=1
            elif(self.z<mn.z):
                self.velZ+=1
    
    def energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z))*(abs(self.velX)+abs(self.velY)+abs(self.velZ))
    
    def tostring(self):
        print(f"pos< x={self.x}, y={self.y}, y={self.z}> vel< x={self.velX}, y={self.velY}, z={self.velZ}>")
    
    def checkAxisX(self):
        if self.startX==self.x and self.velX==0:
            return True
        return False  
    
    def checkAxisY(self):
        if self.startY==self.y and self.velY==0:
            return True
        return False
    
    def checkAxisZ(self):
        if self.startZ==self.z and self.velZ==0:
            return True
        return False

moons=[]
moons.append(Moon(17,5,1))
moons.append(Moon(-2,-8,8))
moons.append(Moon(7,-6,14))
moons.append(Moon(1,-10,4))
#moons.append(Moon(-1,0,2))
#moons.append(Moon(2,-10,-7))
#moons.append(Moon(4,-8,8))
#moons.append(Moon(3,5,-1))

def step():    
    for mn in moons:        
        mn.changeVel(moons)            
    for mn in moons:
        mn.changePos()

cnt=0
axisPeriod=[0,0,0]
while True:
    cnt+=1    
    step()
    if axisPeriod[0]==0 and all([mn.checkAxisX() for mn in moons ]):                
        axisPeriod[0]=cnt
        print(cnt, "=>", axisPeriod)
    if axisPeriod[1]==0 and all([mn.checkAxisY() for mn in moons ]):                
        axisPeriod[1]=cnt
        print(cnt, "=>", axisPeriod)
    if  axisPeriod[2]==0 and all([mn.checkAxisZ() for mn in moons ]):                
        axisPeriod[2]=cnt
        print(cnt, "=>", axisPeriod)    
    if min(axisPeriod)>0:
        break





result =numpy.lcm.reduce(axisPeriod)

print("2019-Day12-B result:", result)
#307043147758488
puzzle.answer_b = result
