from progression import Progression 

class ArithmeticProgression(Progression):
    def __init__(self, increment = 1, start = 0):
        '''create a new arithmetic progression'''
        super().__init__(start)
        self._increment = increment 

    def _advance(self):
        '''update current value by adding the fixed increment'''
        self._current += self._increment 
        

if __name__ == '__main__':
    print('arithmetic progression with increment of 5:')
    ArithmeticProgression(5).printProgression(10)
    ArithmeticProgression(5, 2).printProgression(10)

    for value in ArithmeticProgression(5).printProgression(10):
        print(value * 2)