class Animal:
    def __init__(self, legs = 0):
        '''create Animal object with legs'''
        self.legs = legs

    def walk(self) -> None:
        print(f'This animal walk with their {self.legs} legs')
    
    def sleep(self) -> None:
        print(f'Different animals have different sleeping habits')

    def __repr__(self) -> str:
        return f'Animal: don\'t know\nNumber of legs : {self.legs}'

# MAIN PROGRAM
if __name__ == '__main__':
    anim = Animal(6)
    print(anim)
    
    print()
    anim.walk()
    anim.sleep()