def birthday():
    d = {}
    lst= []
    entry = ''

    while entry != 'stop':
        birthday = input(f'month day name :').split()
        entry.append(birthday[0])
        print(entry)


birthday()