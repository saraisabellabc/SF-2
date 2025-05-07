from pet import Pet
from bird import Bird
from omnivore import Omnivore 

class Parrot(Bird, Omnivore, Pet): 
    def __init__(self, legs = 2, wings = 2, colour = 'yellow'): 
        super().__init__(self, legs) 
        self.wing = wings 
        self.coloour = colour

    def __repr__(self) -> str:
        result = "\nSpecies : Bird"
        result = Bird.__repr__(self) + result  
        result += '\n' + Pet.__repr__(self)     
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Parrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs."'
        
        return super().reproduce() + '\n' + result
    
    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even use a unique method called "beakiation" to traverse narrow branches.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.')
        
    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat both plant and animal matteer. My natural diet includes a variety of foods like seeds, nuts, fruits vegetables, flowers, birds, and insects.')
        
if __name__ == '__main__':
    b1 = Parrot()
    print(b1)

    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

    print()
    b1.eat()

