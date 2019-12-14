from aocd.models import Puzzle


puzzle = Puzzle(year=2019, day=12)

data = puzzle.input_data.split("\n")
print(data)

#seru na to vtupni data prepisu natvrdo :-)

class Moon:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.velX=0
        self.velY=0
        self.velZ = 0

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


moons=[]
moons.append(Moon(17,5,1))
moons.append(Moon(-2,-8,8))
moons.append(Moon(7,-6,14))
moons.append(Moon(1,-10,4))

for i in range(1000):
    print("=================================================")
    print(f"step:{i}")
    for mn in moons:
        mn.tostring()
    for mn in moons:        
        mn.changeVel(moons)
    
    for mn in moons:
        mn.changePos()

        
result = sum([x.energy() for x in moons])

print("2019-Day11-A result:", result)
#6029334
puzzle.answer_a = result
