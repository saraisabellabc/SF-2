from __future__ import annotations # holding Point to be built
import math
class Point: 
    def __init__(self, x: int, y: int):
        self.x = x 
        self.y = y

    def translate(self, dx: int, dy:int) -> None:
        '''Move this Point dx horizontally and dy vertically'''
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other_point: Point )-> float: # returns of type point, but other_point : Point doesnt work because not built -> from __future__ import annotations
        '''return distance between this Point and other_point'''
        a = (other_point.x - self.x)** 2 
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a + b)
    
    def __repr__(self) -> str:
        '''return x, y coordinates of Point as (x, y)'''
        return f'({self.x}, {self.y})' #self of the x and y attribute 
    
    def __lt__(self, other_point: Point) -> Point: # when __ its special 
        # lt -> less than  <
        '''return True if this Point and other_point are of type Point 
        and x, y of this Point is less than the x, y of the other_point'''
        return isinstance(other_point, Point) and\
            self.x < other_point.x and self.y < other_point.y # other_point is a point 

    def __eq__(self, other_point: Point) -> Point: # when __ its special 
        # eq -> equality ==
        '''return True if this Point and other_point are of type Point 
        and x, y of this Point is less than the x, y of the other_point'''
        return isinstance(other_point, Point) and\
            self.x == other_point.x and self.y == other_point.y # other_point is a point 

#class Segment:

# MAIN PROGRAM:
p1 = Point(2, 3) 
# print(f'({p1.x}, {p1.y})')

print(p1) 
# looks what object type is (Point) it goes into class and goes straight to __repr__

p1.translate(3, 7)
# print(f'({p1.x}, {p1.y})')

p2 = Point(5, 6)
print(p1.distance(p2))

p3 =Point(0, 3)
p4 = Point(8, 3)

print('p3 <? p4:', p3 < p4)
print('p3 ==? p4:', p3 == p4)