# number1 = int(input('first number:'))
# number2 = int(input('second number:'))
# result = number1 / number2
#Value error because not int 
#division error at second number is 0

flag = True
while flag:
    try:
        number1 = int(input('first number:'))
        number2 = int(input('second number:'))
        result = number1 / number2  
    except ZeroDivisionError:
        print('attempted to divide by 0 \n')
    except ValueError:
        print('attempted to put another type instead of int\n')
    else:
        print(f'{result: .2f}')

