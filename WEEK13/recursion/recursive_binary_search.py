def binarySearch(lst, low, high, target):
    if high >= low:
        mid = (high + low)//2

        if lst[mid] == target: # found target 
            return mid
        elif lst[mid] > target: # search in left half
            return binarySearch(lst, low, mid-1, target)
        else:   # search target in right half 
            return binarySearch(lst, mid+1, high, target)
    else:
        return -1
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
elem = 5
result = binarySearch(lst,0, len(lst)-1, elem)

if result != -1:
    print(f'element {elem} is present at index {result}')
else:
    print(f'element {elem} is not present')


