from pet import Pet
from omnivore import Omnivore
from mammal import Mammal

class Dog(Mammal, Omnivore, Pet ):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        self.ears = ears 

    def __repr__(self) -> str:
        result = "\n Species : Dog "
        result = Mammal.__repr__(self) + result  # kingdom, class, species
        result += '\n' + Pet.__repr__(self)     # from pet
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Dogs can reproduce'
        return super().reproduce() + '\n' + result
    
    def move(self) -> None:
        print('I move by walking and running')

    def sleep(self) -> None:
        print('Dogs sleep when they are tired')
        
    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat my food and sometimes human food')
        
if __name__ == '__main__':
    b1 = Dog()
    print(b1)

    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

