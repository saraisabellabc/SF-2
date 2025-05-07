from animal import Animal 
class Bird(Animal):
    def reproduce(self) -> str:
        result = 'Birds typically reproduce y hatching and incubating their eggs.'
        
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Bird'