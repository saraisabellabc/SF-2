print('You are to enter two numbers, which I will divide for you')
print('Enter \'q\' to quit anytime.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break

    second_number = input('Second number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) / int(second_number)
        print(f'The result is:{result}')
    except ZeroDivisionError:
        print('You cannot divide by 0')
 #   else:   # execute if try block succeeds
   #     print(f'The result is:{result}')


    
