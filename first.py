class vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def add(self,v):
       return vector2D(self.x + v.x, self.y + v.y)
    def display(self):
         print("(", self.x, ",", self.y,")")    
         
v1 = vector2D(2,3)
v2 = vector2D(4,5)
v3 = v1.add(v2)

v3.display()              
    
    
    