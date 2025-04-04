'''
GIven a dictonnary of keys that are strings and/or integers, values are lists , writea  
snippet of cide that returbs total numbers of eleements of all lists that have keys as strings.


example:
d = {3: [3, 6], 'a' : [3, 4 , 5], "b" : [7, 8, 91, 1]}
prints put a  7
'''
d = {3: [3, 6], 'a' : [3, 4 , 5], "b" : [7, 8, 91, 1]}
num_elements = 0
for key in d:
   
    if type(key) == str:
        num_elements += len(d[key])
print(num_elements)

'''write a fun ction word Tally tahtt takes an integer argument n and reads n words from the user. 
Note that the user may enter the same word multiple times. '''
def wordTally()


'''
d = {3: 5, 4:5, 6:1}

d_inverted = {5:[3, 4], 1 :[6]}
'''

def inverted(d):
    d_inverted = {}
    for key in d:
        for value in d:
            return d

