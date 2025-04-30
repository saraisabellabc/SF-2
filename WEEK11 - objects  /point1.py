class Point: # construct doesnt return, it builds 
    def __init__(self): # all functions have self as an argument
        ''' create two-dimensional point (0,0)'''
        self.x = 0
        self.y = 0


# MAIN PROGRAM:
p1 = Point() # goes into class and immediatly calls init function 
print(f'({p1.x}, {p1.y})')