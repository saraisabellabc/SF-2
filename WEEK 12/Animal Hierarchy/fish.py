from __future__ import annotations
from animal import Animal


class Fish(Animal):
    def __init__(self, colour):
        #super().__init__(0)
        self.type = 'fish'
        self.colour = colour

    def walk(self) -> None :
        print('Fish do not walk they swim')

    def sleep(self) -> None:
        print('Fish rest by reducing their activity and metabolism')

    def __repr__(self) -> str:
        return f'Animal: {self.type}\nColour : {self.colour}'
    
    def changeColour(self, colour) -> None:
        self.colour = colour

    def sameColour(self, other_fish: Fish) -> bool:
        return self.colour == other_fish.colour

    
if __name__ == '__main__':
    fish = Fish('blue')
    print(fish)

    print()
    fish.walk()

    fish.changeColour('Yellow black stripped')
    print(fish)

    print()

    fish2 =Fish('pink')
    print(fish2)
    print(fish.sameColour(fish2))

# according to the code that we have it 
# how do you know its inherinitng from Object : __repr__ __lt__ 
# you are overwritting