lst = input().split()
N = int(lst[0])
M = int(lst[1])
D = int(lst[2])
schedule = input().split()
schedule = [ int(x) for x in schedule].sort()
clean = N 
dirty = 0 
laundry = 0
for i in range(D):
    clean-= 1 
    dirty += 1
    temp = i + 1
    if temp in schedule:
        clean += 1 
    if len(clean) == 0:
        laundry += 1 
        clean = dirty 
        dirty = 0
print(laundry)