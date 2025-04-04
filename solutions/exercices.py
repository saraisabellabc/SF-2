t = ('apple', 17.3, [99, 98])  
tup = (t[2], ) + (3, ['apricot', 'pear'])  
tup[2] = ['tomato']  
print(tup)