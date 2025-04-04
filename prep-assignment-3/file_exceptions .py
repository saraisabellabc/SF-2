file = 'book.txt'


try:
    input_file = open(file, 'r')
except FileNotFoundError:
    print(f'Sorry, the file {file} does not exist')
    output_file = open(file, 'w', encoding = 'UTF8')
else:
    for line in input_file:
        print(line.rstrip())
input_file = open('hello', 'r', encoding = 'UTF8')
hello_lst = input_file.readlines()
output_file.writelines(hello_lst)

input_file.close()
output_file.close()