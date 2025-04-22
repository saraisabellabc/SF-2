# has a relationship -> is a relationship 
# i want cat to inherit and pick and chose

from animal import Animal 

class Cat(Animal):
    def __init__(self):
        super().__init__(4) # Will have 4 legs Cat in sub class/child/descendant Animal is super/parent/ascent..
        #self.legs
        self.type = 'cat' # i didnt have type in animal so its additional 
    
    def sleep(self, hours = None) -> None:
        if hours == None:
            print('Cats sleep in warm and comfortable places')
        else:
            print('Cats can sleep for {hours} hours daily')
        
    def __repr__(self) -> str:
        return f'Animal : {self.type}\nLegs: {self.legs}'
    
# if we write here a function we overwrite the functions 

# MAIN PROGRAM 
if __name__ == '__main__': # the current script that you are running (cat.py) is at the current program
    cat = Cat()
    print(cat) #

    print()
    cat.walk() # will go higher in the hierarchy/parent class and tries to find the method we are looking for 
    cat.sleep()
    cat.sleep(12)
'''
Output without if name = main :
This animal walk with their 6 legs
Different animals have different sleeping habits
Animal : cat
Legs: 4

This animal walk with their 4 legs
Cats sleep in warm and comfortable places
Cats can sleep for {hours} hours daily
'''
