def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid] # no + 1 
    right_half = lst[mid:] # creating new lists

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    lst = []
    i = j = 0   # i pointer to left, j pointer to right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1 

    lst.extend(left[i:])
    lst.extend(right[j:])
    return lst



unsorted_lst = [3, 7, 6, -10, -3, 15, 23.5, 55, -13]
sorted_lst = mergeSort(unsorted_lst)
print(f'Sorted List : {sorted_lst}')



# run time is nlogn 
# height of the tree : logn , because look at the binary tree  or constant children (0 or 2 children)n, all the levels are practically full


