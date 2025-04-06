#Two questions

#Difficult Tuple Tracing Question
def modify_tuple(t):
    x, y, z = t 
    new_t = (z, x + y, y - z) 
    return new_t 

tuple = ((5, 2, 8), (3, 6, 1), (4, 9, 7)) 
lst =  [] 
for i in tuple: 
	lst.append(modify_tuple(i)) 

print(lst[1][2] + lst[2][0])


#Medium 2D List Tracing Question 
lst = [[2, 4, 6], [1, 3, 5], [7, 9, 11]]
for i in range(len(lst)):
	for j in range(len(lst[i])): 
		if i == j: 
			lst[i][j] *= -1 
		elif i < j: 
			lst[i][j] += lst[j][i] 
for row in lst: 
	print(row)
