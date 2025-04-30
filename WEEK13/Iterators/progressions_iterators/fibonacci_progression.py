from progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 0):
        super().__init__(first)
        self._prev = second - first # value preecceding first 

    def _advance(self):
        self._current = self._prev + self.first 
        # updating and resetting prev 
        pass

if __name__ == '__main__':
    FibonacciProgression().printProgression(10)
    ...