def binarySearch(lst, target):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:  # while still space to search
        mid = (low + high ) // 2

        if lst[mid] < target: # target is in the right half
            low = mid + 1
            print(f'Looking for {target} in list {lst[low:high+1]}')

        elif lst[mid] > target: # target is in the left half 
            high = mid - 1
            print(f'Looking for {target} in list {lst[low:mid]}')
        else:
            return mid
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
elem = 5
result = binarySearch(lst, elem)

if result != -1:
    print(f'element {elem} is present at index {result}')
else:
    print(f'element {elem} is not present')

'''
if its less, right if its bigger, left 
'compare' while loop iteration = nmbr of time its compared
high of the tree : run time -> logn 
why ? 2^0 2^1 2^2 2^3
2^n+1 = n+1
-> log(2^n+1) = log(n + 1)
(n+1)lg2 = lg(n+1)
-> n = lg(n+1) - 1

show lg(n+1)-1 e O(lgn)
'''


        


