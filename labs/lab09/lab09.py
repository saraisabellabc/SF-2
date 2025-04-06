# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value is 
the balance.  Print the final dictionary.  
'''

output_file = open('accounts.txt', 'w')
for i in range(5):
     line = input('accounts info: ')
     output_file.write(line + '\n')
output_file.close()

d_outer = {}
d_inner = {}
for line in output_file:
     line = line.rstrip().split()   # line is a list of account number, name, balance
     account_num = line[0]
     name = line[1]
     balance = line[2]

    #  line = line.rstrip()
    #  account_num, name, balance = line.split()

     d_inner[line[1]] = line[2]
     d_outer[line[0]] = d_inner

     #d_outer[line[0]] = {line[1]: line[2]}

print(d_outer)

# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

'''
output_file = open('grades.txt', 'w')
for i in range(3):
     firstname, lastname, exam1grade, exam2grade, exam3grade = input('Grade information : ').split()
     output_file.write(firstname + ',' + lastname + ',' + exam1grade + ',' + exam2grade + ',' + exam3grade + '\n')
output_file.close()


'''

(b) Once your grades.txt file is populated, read and store the infomration
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''
# store data 
output_file = open('grades.txt', 'r')
d_info = {}
for line in output_file:
    firstname, lastname, exam1grade, exam2grade, exam3grade = line.strip(',,').split()
    d_info[(firstname, lastname)] = [int(exam1grade), int(exam2grade), int(exam3grade)]

#b)
#i) ii) iii)
for i in range(3):
     for value in d_info.values() :
        mini = min(value[i])
print(mini)

for i in range(3):
     for value in d_info.values() :
        maxi = max(value[i])
print(maxi)

for i in range(3) :
    grades = (d_info.values()) / len(d_info)
    for value in grades:
        averages_exam =sum(value[i])


for student in d_info:
    average_student = sum(d_info[student ]) / 3 

print(averages_exam)
print(average_student)





# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

'''
output_file = open('words.txt', 'r')
input_file = open('words_updated.txt' , 'w' )
for line in output_file :
    input_file.write(line.replace('\n', ' '))
output_file.close()
input_file.close()
    


'''

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''
num_words = 0
for line in output_file :
    num_words =+ 1 
k = input('Integer between 1 and 80 :')
