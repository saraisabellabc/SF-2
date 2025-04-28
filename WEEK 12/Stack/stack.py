from __future__ import annotations
from functools import total_ordering

import time 
ESC = '\x1b'
YELLOW = ESC + '[33m'
BLUE = ESC + '[34m'
PURPLE = ESC + '[35m'
GREEN = ESC + '[32m'
RED = ESC + '[31m'
RESET = ESC + '[0m'
WHITE = ESC + '[37m'



class Empty(Exception):
    '''error attempting to access an element from an empty container'''
    pass

@total_ordering
class Stack:
    def __init__(self):
        self.__data = []   # index 0 is bottom of stack, index -1 is top of stack
        # self.data will be accessible, __ 2 underscore will make it private to the class only (cant access it from outside of the class)
        # one underscore _ : can be accessed by descendance of the class ?

    def __len__(self) -> int:
        '''return length of stack'''
        return len(self.__data)
    
    def isEmpty(self) -> bool:
        return len(self.__data) == 0 # or len(self) calling the function
    
    def push(self, elem: object) -> None:
        '''add element elem to the top of the stack
        doc test : working with python shell in a doc string
        >>> s = Stack()
        >>> s.push(5) 
        >>> s.push(3)
        >>> s.pop()
        3
        '''
        self.__data.append(elem)

    def top(self):
        '''return the element at the top of the stack but not remove '''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data[-1]
    
    def pop(self):
        '''remove the element at the top of the stack and return its value '''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data.pop() # function on a list, on last element 
    
    # def __repr__(self) -> str:
    #     return ' '.join(list(map(str, self.__data)))

    def __repr__(self) -> str:
        width = 20  # total width for the whole line
        inner_width = width - 4  # space between the bars: 2 for "|" and 2 for padding

        if self.isEmpty():
            return (WHITE + "|" + "  ".center(inner_width) + "|" + '\n' +
                    "-" * width + RESET)

        lines = []


        top = f"| {str(self.__data[-1]).center(inner_width)} |"
        lines.append(PURPLE + top + RESET)
        lines.append("-" * width)


        for i in range(len(self) - 2, -1, -1):
            line = f"| {str(self.__data[i]).center(inner_width)} |"
            lines.append(RED + line + RESET)
            lines.append("-" * width)

        return '\n'.join(lines)
    # def __repr__(self):

    #     stack = print(f'|' + self.__data[-1] + '|' + '\n' + '----------')
    #     for i in range(len(self) - 1):
    #         stack = print(f'|' + self.__data[i] + '|' + '\n' + '----------')
    #     if self.isEmpty():
    #         RESET + stack
    #     else:



    
    def __lt__(self, other: Stack) -> bool:
        '''less than elements '''
        return len(self.__data) < len(other)

    def __eq__(self, other: Stack) -> bool:
        '''equal len'''
        return len(self.__data) == len(other)
    
    def isMatched(self, s: str) -> bool:
        st = Stack()
        pairs = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in pairs.values():       
                st.push(ch)
            elif ch in pairs:              
                if st.isEmpty() or st.pop() != pairs[ch]:
                    return False
            else:
                continue

        return st.isEmpty()



            

            


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose = True)
    S = Stack()
    # print(S)
    # time.sleep(2)
    
    # S.push(5)
    # print(S)
    
    # S.push(3)
    # print(S)
    # # print(len(S))
    

    # print('pop -- ', S.pop())
    # # print(S.isEmpty())
    # print(S)
    # time.sleep(2)

    # print('pop -- ', S.pop())
    # print(S)
    # time.sleep(2)

    print(S.isMatched('())]}'))


# # is printing True 

    
    
