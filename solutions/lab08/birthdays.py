def birthday():
    d = {}
    lst= []
    entry = ''

    while entry != 'stop':
        birthday = str(input(f'month day name :')).split()

        month = birthday[0]
        day = birthday[1]
        name = birthday[2]
        inner_d = {}
        #inner_d[birthday[1]] = n

        d[birthday[0]] = inner_d
        


        

        d[entry] = inner_d
birthday()