'''
We are given n unopened boxes with k number of figurines in each box. The boxes cannot be opened and hence, the order of the figurines cannot be changed.
A box cannot be rotated (otherwise the figurines will be facing the wrong way)

Each figurines is specified by its height.
For example, in a given box the height og the figurines from left to right 4, 5, and 7.
Note that the number of figurines in each box may vary.

We would like to organize all the toy boxes such that they are arranged in non-decreasing order of figurine heights from left to right.
However, this may not necessarily be possible with the given boxes. Hence, write a program to determine if we can have such an arrangement or not.

Assume k is not empty, k> 1

INPUT SPECIFICATION:
- first line of input: integer n representing the number of toy boxes
- next n lines: one for each box. Each of these lines begin with:
    --> integer k indicating the number of figurines int the box ( k>=1)
    --> followed by k integers giving the height of figurines from left to right seperated by a space
    Each height is an integer value >= 1

OUTPUT SPECIFICATION:
YES if we can organize the boxes
NO otherwise 
'''
'''
Top-Down Design : captures main tasks of your solution
--> some taskes will not require much code
    => will solve them directly
--> other tasks wil require more from us 
    => will define a function
'''
# 2. Function definition
def readBoxes(n):
    lst_boxes =[]
    for i in range(n):
        box = input().split() #[ '3', '4', '5', '7']
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i]) # turn stings into integers
        lst_boxes.append(box)
    return lst_boxes 

def allBoxesOk(lst_boxes):
    for box in lst_boxes:
        if box != sorted(box): #box.sort() changes 
            return False
        return True
    
def boxIntervals(lst_boxes):
    intervals = []
    for box in lst_boxes:
        intervals.append([box[0], box[-1]]) # appending a list, not single values

    return intervals 

def allIntervalsareOK(lst_intervals):
    prev_max_height = lst_intervals[0][1] 

    for box in range(1, len(lst_intervals)):
        curr_min_height = lst_intervals[box][0]
        if curr_min_height < prev_max_height:
            return False 
        prev_max_height = lst_intervals[box][1]
    return True 


 
 #3. MAIN program


# 1. Write TODOs

# read input
n = int(input('number of boxes:'))
boxes = readBoxes(n)


# check if all boxes are okay (in non-decreasing order)
if not allBoxesOk(boxes):
    print('NO')

else:

    # obtain a new list of boxes with only 
    # the left and right heights (intervals)
    intervals = boxIntervals(boxes)

    # TODO : sort the boxes (i. e. intervals)
    intervals.sort() # .sort() : sorts by the first elemnt, if the same goes into the second one 


    # TODO: determine whether the boxes are organized of not 
    if allIntervalsareOK(intervals):
        print('YES')
    else:
        print('NO')
