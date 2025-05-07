'''
sorting algorithm 
best case run t: logn
avg run time : nlogn
worst : n^2

1. find pivot, partition around the list (2) around the pivot 
ex. pivot : 15 - everything less than -> left everything greater than -> right

finding pivot : 
- randomisation 
partitions: less than half , equal , greater than half
2. recurse on both partitions
3. merge 

deterministic quick sort:
- always same answer, recursion tree 

EX. 
85 24 63 45 17 31 96 50
taking pivot as last element : 50
                50 
 24 17 31        85 63 96

 !recurse 
 combining : > = <   concatenate them 

 --> make it inplace : swap the elements without creating new containers 



'''