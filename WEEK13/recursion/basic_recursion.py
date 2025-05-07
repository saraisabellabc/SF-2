# within its def its calling itself 
def iterSum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# the recursion tree 
# cirlce vertices
def recSum(n):
    if n == 1:
        return 1
    else:
        return recSum(n-1) + n
# run time is O(n), bc 
# when a function returns it gets poped out of the memory stack 

def recFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recFactorial(n-1) * n
    
# to compute f(5) have to compute f(4) + f(3) etc.
def badFibonacci(n):

    #   HW  exceptions 
    if n == 0 or n == 1:
        return n
    else:
        return badFibonacci(n-1) + badFibonacci(n-2)
    # crash if -1 when rans out fo momwry

#   HW  
def goodFibonacci(n):
    pass
#constant 

# why is it log n





