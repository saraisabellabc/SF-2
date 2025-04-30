from __future__ import annotations 
from point import Point # the class name 

class Segment: # segment is NOT A point, it HAS a point
    '''line segments'''
    def __init__(self, p1: Point, p2: Point):
        '''create segment between p1 and p2'''
        self.p1 = p1
        self.p2 = p2 
    
    def translate(self, dx: int, dy:int) -> None:
        '''move segment by dx horizontaly and dy vertically'''
        self.p1 .translate(dx, dy)
        self.p2.translate(dx, dy )
    
    def length(self) -> float:
        '''return length of segment'''
        return self.p1.distance(self.p2)
    
    def __lt__(self, other_segment: Segment) -> bool:
        return isinstance(other_segment, Segment) and \
            self.length() < other_segment.length()
    # returns false without isinstance

# MAIN PROGRAM
p1 = Point(2, 5)
p2 = Point(4, 2)
p3 = Point(0, 0)
p4 = Point(11, 12)

line1 = Segment(p1, p2)
line2 = Segment(p3, p4)
print(f'length of line1: {line1.length()}')
print(f'length of line2: {line2.length()}')
print(line1 < line2)