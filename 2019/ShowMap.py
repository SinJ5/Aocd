'''
Created on 15. 12. 2019

@author: j
'''
class ShowMap:
    def __init__(self,legend):
        self.legend=legend
    
    def makeFrame(self,data):
        tmpX=[pos[0] for pos in data.keys()]
        tmpY=[pos[1] for pos in data.keys()]
        minX=min(tmpX)
        minY=min(tmpY)
        maxX=max(tmpX)
        maxY=max(tmpY)
        self.frame =  [[" "for x in range(maxX-minX+2)] for y in range(maxY-minY+2)]
        for pos,val in data.items():
            self.frame[pos[1]-minY][pos[0]-minX]=self.legend[val]
    
    def draw(self):
        for data in self.frame:
            print("".join(data)) 