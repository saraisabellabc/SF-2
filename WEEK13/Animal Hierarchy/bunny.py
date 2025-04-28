from pet import Pet
from mammal import Mammal 
from herbivore import Herbivore 

class Bunny(Mammal, Herbivore, Pet): # the order of priority 
    def __init__(self, legs = 4, ears = 2): # if just legs it would print a 0 
        super().__init__(legs) # it will go in Mammal 
        #Mammal.__init__(self, legs)
        self.ears = ears 

    def __repr__(self) -> str:
        result = "\n Species : Bunny "
        result = Mammal.__repr__(self) + result  # kingdom, class, species
        result += '\n' + Pet.__repr__(self)     # from pet
        return result + '\n' + Herbivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Bunnies can reproduce multiple litters per year\
            potentially having 3-8 kits per litter'
        
        return super().reproduce() + '\n' + result
    
    def move(self) -> None:
        print('I move by hopping and I can see behind me...')

    def sleep(self) -> None:
        print('Bunnnies as noctural animals, typically\
              sleep around 12 to 14 hours aday in short,\
              intermittent periods.')
        
    def eat(self) -> None:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass, with\
              some leafy greens and few pellets. I should\
              only be given fruit and root vegetables\
              like carrots and an occasional treat.')
        
if __name__ == '__main__':
    b1 = Bunny()
    print(b1)

    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

