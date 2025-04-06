'''
Quetion 1: Create Pascal's Triangle more efficiently than O(n^3)-time and
O(n^2) space.  
'''

'''
Question 2: ToyBoxes
'''


'''
Question 3: Baker Bonus
problem statement already online
'''

'''
Question 4: Unique Paths
Given a m by n matrix, you are to determine and print the 
number of unique paths starting at the top left corner and
ending at the bottom right corner of the matrix.  The only
possible moves that can be made are either a move to the
right or down. 

Example-1: 

      0  1
[0   [x, x],
 1   [x, x]  ]

path 1: (0, 0) --> (0, 1) --> (1, 1)
path 2: (0, 0) --> (1, 0) --> (1, 1)

=> output: 2


Example-2: 

      0  1  2
[0   [x, x, x],
 1   [x, x, x],
 2   [x, x, x]  ]

path 1: (0, 0) --> (0, 1) --> (0, 2) --> (1, 2)
path 2: (0, 0) --> (0, 1) --> (1, 1) --> (1, 2)
path 3: (0, 0) --> (1, 0) --> (1, 1) --> (1, 2)

=> output: 3
'''

'''
Question 5: 
Update Pascal's Triangle code so that your algorithm uses only O(1) space.  
'''




'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''


'''
Question2:

Write a function wordTally that takes an integer argument 
n and reads n words from the user.  Note that the user
may enter the same word multiple times.  
Your function should tally up how many times each word
occurs that the user has entered and store it in a dictionary
where the keys are the words and the values are the number
of times each word occurs.  
Return this dictionary. 

You may only create one collection: one dictionary
'''


'''
Quesiton3: 

write a function called invertDictionary that takes a 
dictionary d as an argument.  This function inverts the
provided dictionary.  That is, the keys become the values
(as lists) and the values become the keys. 

Note that d may have repetitive values, in which case in 
the inverted dictionary only one of these values
will be used as a key. For such a key, in the inverted
dictionary the value is a list of all such possible
keys from d

For example: 
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''

'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''