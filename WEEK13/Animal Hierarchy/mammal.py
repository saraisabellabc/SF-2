from animal import Animal 
class Mammal(Animal):
    def reproduce(self) -> str:
        result = 'Mammals give birth young to live young, and raise them\
            until they can be indepedent'
        
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Mammal'