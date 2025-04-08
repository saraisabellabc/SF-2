# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

# input_file = open('story.txt', 'r')
# count = 0
# words = {}
# for line in input_file:
#     count += len(line.split())
#     lst = line.split()
#     for word in lst:
#         word = word.lower().strip(" .,-()!?'\"")
#         words[word] = words.get(word, 0) + 1
# input_file.close()
# print(f' Word count :{count} \n')



# print(f'\nWord count :{count} ')

# new_dict = {}
# for word in words:
#     new_dict[words[word]] = word
# for key in sorted(new_dict.keys(), reverse = True):
#     print(f'{new_dict[key]} : {key}')

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

# cats_file = open('cats.txt', 'r')
# dogs_file = open('dogs.txt', 'r')
# for line in cats_file:
#     print(line)
# for line in dogs_file:
# #     print(line)

# try:
#     cats_file = open('cats.txt', 'r')
# except FileNotFoundError:
#     pass
#     #print(f'The file does not exist')
# try:
#     dogs_file = open('dogs.txt', 'r')
# except FileNotFoundError:
#     pass
#     # print(f'The file does not exist')
# # Question 3

'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''

try:
    first_number = int(input("First number: "))
    second_number = int(input("Second Number: "))
except ValueError:
    print("Enter a numerical value")
else:
    print(f"Sum: {first_number + second_number}")
# Question 4
'''
Using the json module write student information to the file in JSON format.  
That is, create a dictionary of of student data in the following format: 
gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}. 

Each dictionary in the list represents one student and contains the keys:
'first_name', 'last_name', 'exam1', 'exam2' and 'exam3'.  The keys map to the
values represengint each student's first name (string), last name (string) and 
three exam scores (integers).  

Output the gradebook_dict in JSON format to the file grades.json.  
'''
import json

output_file = open('grades.json', 'w')
list_d = []
while True:
    line = input("'first_name' 'last_name' 'exam1' 'exam2' 'exam3' (or q to quit)")
    if line == 'q':
        break
    first_name, last_name, exam1, exam2, exam3 = line.split()
    d = {'first_name': first_name, 'last_name': last_name, 'exam1': int(exam1), 'exam2': int(exam2), 'exam3': int(exam3)}
    list_d.append(d)
    
json.dump(list_d, output_file)
output_file.close()
# Question 5
'''
Using the json module to read the grades.json file created in the previous
question.  Display the data in tabular format, including an additional 
column showing each student's average to the right of the student's three
exam grades and an additional row showing the class average on each exam.  '
'''