class Point: # only one constructer allowed in pyhton 
    # if there is more than 1, ITS ONLY TAKING THE LAST ONE 
    def __init__(self): 
        ''' create two-dimensional point (0,0)'''
        self.x = 0
        self.y = 0

    def __init__(self, x: int, y: int):
        self.x = x # setting attributes to the object
        self.y = y




# MAIN PROGRAM:
p1 = Point() 
print(f'({p1.x}, {p1.y})')