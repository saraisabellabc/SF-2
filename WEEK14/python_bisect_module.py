'''
--> lst to work with
--> num want to insert into the lst
--> [start, end] interval of the lst to consider
(defaulted to the entire lst)

>>> import bisect
>>> lst = [1, 2, 7, 7, 7, 8, 10, 11]
>>> bisect(lst, num, start, end)
5

returns the index where num can be inserted into lst so that lst is sorted 
if num already in the lst, returns rightmost index where num
can be inserted

>>> bisect_left(lst, num, start, end)
>>> 2

returns the index where num can be inserted into lst so that lst is sorted 
it  num already in lst, returns left most index where num can be inserted

>>> bisect_right(lst, num, start, end)
5

'''

import bisect 
lst = [1, 2, 7, 7, 7, 7, 8, 10, 11]
num = 7


print(bisect.bisect(lst, num))
print(bisect.bisect_right(lst, num))
print((bisect.bisect_left(lst, num)))