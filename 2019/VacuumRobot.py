'''
Created on 17. 12. 2019

@author: j
'''
SCAFOLD=35
VACUUM=46
UP =0
RIGHT =1
DOWN =2
LEFT =3


NL=10

class pathFinderForVacuumRobot(object):
    '''
    classdocs
    '''


    def __init__(self, maps):
        '''
        Constructor
        '''
        self.maps=maps
        self.sequence=[]
        self.pos=None
        self.dir=None
        self.step=0
        self.getStartPos()
    
    def getStartPos(self):
        for pos,val in self.maps.items():
            if val > VACUUM:
                self.pos=pos
                self.dir=0
                break;
    
    def getNextPos(self):
        if self.dir ==UP:
            return (self.pos[0],self.pos[1]-1)
        if self.dir ==DOWN:
            return (self.pos[0],self.pos[1]+1)
        if self.dir ==LEFT:
            return (self.pos[0]-1,self.pos[1])
        if self.dir ==RIGHT:
            return (self.pos[0]+1,self.pos[1])
    
    def getNextVal(self):
        pos =self.getNextPos()
        if pos in self.maps.keys():            
            return self.maps[pos]
        return VACUUM
    
    def checkNextVal(self):
        return self.getNextVal()==SCAFOLD
    
    def moveNext(self):
        if self.dir ==UP:
            self.pos=(self.pos[0],self.pos[1]-1)            
        if self.dir ==DOWN:
            self.pos=(self.pos[0],self.pos[1]+1)
        if self.dir ==LEFT:
            self.pos=(self.pos[0]-1,self.pos[1])
        if self.dir ==RIGHT:
            self.pos=(self.pos[0]+1,self.pos[1])
    
    def checkPos(self):
        if self.dir ==UP or self.dir ==DOWN :
            pos1=(self.pos[0]+1,self.pos[1])
            pos2=(self.pos[0]-1,self.pos[1])                                                
        if self.dir ==LEFT or self.dir ==RIGHT :
            pos1=(self.pos[0],self.pos[1]+1)
            pos2=(self.pos[0],self.pos[1]-1)
            
        return (
                    ((pos1 in self.maps) and self.maps[pos1]!=SCAFOLD
                    or  not (pos1 in self.maps)) and
                    ((pos2 in self.maps) and self.maps[pos2]!=SCAFOLD
                    or  not (pos2 in self.maps))                    
                )                
        
    
    def cleanPos(self):
        if self.checkPos():
            self.maps[self.pos]=VACUUM
    
    def checkTurn(self,val):
        ''' 1 RIGHT -1 LEFT'''
        if self.dir==UP:            
            pos=(self.pos[0]+val,self.pos[1])
        if self.dir==DOWN:            
            pos=(self.pos[0]-val,self.pos[1])
        if self.dir==LEFT:            
            pos=(self.pos[0],self.pos[1]-val)
        if self.dir==RIGHT:            
            pos=(self.pos[0],self.pos[1]+val)
        
        
        return  pos in self.maps and self.maps[pos]==SCAFOLD
    
    
    def turn(self):
        if self.checkTurn(1):
            self.sequence.append("R")
            self.dir=(self.dir+1)%4
            return True
        if self.checkTurn(-1):
            self.sequence.append("L")
            self.dir=(self.dir+3)%4
            return True
        print("no turn maybe end")
        self.cleanPos()
        return False
    
    def checkEnd(self):
        return   sum([1 for x in self.maps.values() if x== SCAFOLD])==0
       
    
    def pathFinder(self):
        while not self.checkEnd():        
            if self.checkNextVal():
                self.step+=1
                self.cleanPos()
                self.moveNext()
            else:
                self.sequence.append(str(self.step))
                self.step=0
                if not self.turn():
                    break;
            
        
        return self.sequence
            
            
            
            
            
            