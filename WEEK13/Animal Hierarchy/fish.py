from animal import Animal 
class Fish(Animal):
    def reproduce(self) -> str:
        result = 'Fish reproduction varies largely, some give birth to live young while others lay eggs.'
        
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Fish'