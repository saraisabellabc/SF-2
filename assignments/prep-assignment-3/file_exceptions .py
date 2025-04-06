file = 'book.txt'

try:
    input_file = open(file, 'r')
except FileNotFoundError:
    print(f'Sorry, the file {file} does not exist')
    output_file = open(file, 'w', encoding = 'UTF8')
    #pass 
    #pass means trial block fails silently and doesnt do anything 
else:
    for line in input_file:
        print(line.rstrip())

input_file = open('hello.txt', 'r', encoding = 'UTF8')
hello_lst = input_file.readlines()
output_file.writelines(hello_lst)

input_file.close()
output_file.close()

'''
1) count the number of words in you file (this last file)'

2) make two files : cats.txt and dogs.txt. store at least three names cats in the first file and three names of dogs in the
seocnd file'
write a program that tries to read these files and print the contents of the file to the screen. wrap your code in a 
try-except
block to catch the FileNotFoundError,a nd print a friendly message if a file is missing. move on of the files to a different 
location on your system
, make sure that the code in the except block executes proper

3) modify your previous code fail silently if either file is missing

4) one common problem when prompting for a numerical input tp int. a ValueError occurs . write a program that prompts the user 
for two numbers, add them together and print the result. catch the ValueError  if either input value is not a 
number,a nd print a friendly 
error message . thest your by enteringtwo numbers and then by entering some text instead of a number. 

'''