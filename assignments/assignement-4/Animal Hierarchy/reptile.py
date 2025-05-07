from animal import Animal 
class Reptile(Animal):
    def reproduce(self) -> str:
        result = 'Reptiles reproduce by laying eggs, typically on land rather than water.'
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Reptile'