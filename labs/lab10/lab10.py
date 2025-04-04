# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

input_file = open('labs/story.txt', 'r')
count = 0
words = {}
for line in input_file:
    count += len(line.split())
    lst = line.split()
    for word in lst:
        word = word.lower().strip(".,-()!?'\"")
        words[word] = words.get(word, 0) + 1

print(count)

# max_w = max(words.values())
# for key, value in words.items():
#     if value == max_w:
#         sorted_words[key] = value

lst = []
v = 0
for key, value in words.items():
    if value > v:
        lst.append(words[key])
print(lst)


 



# words = {}
# for line in input_file:
#     list = line.split()
#     print(list)
    





# Question 2
'''
Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
file and three names of dogs in the second file.  Write a program that tries to read
these files and print the contents of each file to the screen.  

(a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
    friendly message if a file is missing.  To test your code, move one of the files 
    to a different location on your system, and make sure that the code in the except 
    block executes properly.  
(b) Modify your previous code to fail silently if either file is missing
'''
# cats_file = open('cats.txt', 'r+')
# dogs_file = open('dogs.txt', 'r+')
# input(cats_file.write()).split()
# input(dogs_file.write()).split()

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''