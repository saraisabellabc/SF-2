class Progression:
    '''iterator producing a generic progression
    
    default iterator : 0, 1, 2, 3 ...
    natural numbers in computer science contain 0
    in maths doesnt '''
    def __init__(self, start = 0): # private, cant access from outside 
        self._current = start
    

    def _advance(self): # protected method of the class, only for the class use not from outside still can but better to 
        '''uodate self._current to a new value
        this should be ovverwritten by a subclass to customize progression'''
        self._current += 1 

    def __iter__(self):
        '''by convention, an iterator must return itself as na iterator'''
        return self 

    def __next__(self):
        '''return the next element or else 
        raise StopIteration error'''
        if self._current is None: # our convention to stop the progression
            raise StopIteration
        else:
            answer = self._current 
            self._advance() # technically could get rid of this function and incorporate here
            return answer 
        
    def printProgression(self, n):
        '''print next n values of the progression'''
        print(' '.join(str(next(self)) for j in range(n))) # could be different 
        # its making a call to advance

    def lstProgression(self, n):
        lst = [int(next(self)) for _ in range(n)]
        return lst
    
if __name__ == '__main__':
    print('Default Progression: ')
    Progression().printProgression(6)
    Progression(12).printProgression(11)

    for value in Progression().lstProgression(10):
        print(value * 2)

    for item in Progression(12):
        print(item)
    # intifinte