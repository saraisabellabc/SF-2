from progression import Progression
'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''
class EvenNumbers(Progression):
    def __init__(self, start, end):
        if start % 2 != 0:
            start += 1
        super().__init__(start)
        self.end = end
    
    def _advance(self):
        self._current += 2
        if self._current > self.end:
            self._current = None

if __name__ == '__main__':
    for item in EvenNumbers(10, 20):
        print(item)

'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self._count = 0
        self._prev, self._current = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count >= self.n :
            raise StopIteration
        self.count += 1
        result = self._prev
        self._prev, self._current = self._current, self._prev + self._current 
        return result 
    
        
        #pay attention to design -> secure/private
'''
Draw the recursion tree for the computation of 
recSum(10)
'''
# the recursion tree 
# cirlce vertices
def recSum(n):
    if n == 1:
        return 1
    else:
        return recSum(n-1) + n
# run time is O(n)
# when a function returns it gets poped out of the memory stack 

'''
write a recursive function that determines the
minimum element in a given list of integers. 
'''
def recMin(lst, start, end):


    if end - start == 1 :
        return lst[start]
    
    else:
        mid = (start + end) // 2
        left = recMin(lst, start, mid)
        right = recMin(lst, mid, end)
        return min(left, right)

lst = [2, 4 , 1, 3, 8, 7]
print(recMin(lst, 0, len(lst)))
        


    


'''
write a recursive function that converts a string of integers
into its integer counterpart
'''

'''
write a recursive function to determine if a given string
is a palindrome
'''

'''
Write a recursive function to count number of vowels in a string
'''

'''
use recursion to determine if a string has more vowels than consonants. 
'''

'''
implement an iterator that filters out even values from a range iterable
'''

'''
'''