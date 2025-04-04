'''
Firgus is behind on several assignements. After rumaging through his backpack , he realizes that he has N items, each of which he records as strings. 
he has M upcoming assignements, the i-th of which requires Ti required items to complete, r1, r2, r3 ... rTi 
if he has all Ti required items, he can complete the i-th assignement. Otherwise, he flunks it .
how mNY ASSIGNEMENTS CAN FIGUS COMPLETE?

INPUT SPECIFICATION:
--> first line contains 2 integers: N and M separated by a space
--> next N lines contaijs a single string si
    it is garanteed that all srings will be unique 
--> next M sections contain a single integer Ti,
which 
is followed by Ti lines each containing a single string ri

OUTPUT SPECIF
output a single integer on a single line,
the answwer to the problem (i. e . the number of assignements firgus can complete)
sample input:
3 4 
chalk
cheese 
charger 
1 
cheese
2 
coins 
cash 
3 
charger 
chalk 
cafe '''


assignements = set()
lst = input().split()
N = int(lst[0])
M =int(lst[1])
for r in range(N):
    assignements.add(input())

print(assignements)

count = 0 
for t in range(M):
    a = int(input())
    subset = set()
    for ti in range(a):
        
        as_done = input()
        subset.add(as_done)
    if subset.issubset(assignements):
       count += 1

print(count)
       

