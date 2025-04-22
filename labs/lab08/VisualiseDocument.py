'''
write a function called combine2 that takes 2 dictionaires d1 and d2
    and combines them together into a new dictionary and returns
    this dictionary.
Here are the details: 
--> d1 and d2 are dictionary of dictionaries.  The inner dictionary
    values are lists of integers
--> if d1 and d2 have the same key, for which the respective inner
    dictionaries both in d1 and d2 also have the same key k, then
    k is added as a key to the  combined dictionary and the value
    is the sum of the values in the respective lists.  

>>> d1 = {'a': {3: [2], 4: [5, 6]}}
>>> d2 = {'a': {3: [8, 12]}}
>>> combine2(d1, d2)
{3: 22}
'''
d1 = {'a': {3: [2], 4: [5, 6]}}
d2 = {'a': {3: [8, 12]}}
def combine2(d1, d2):
    new_d = {}
    for k in d1:
        if k in d2:
            for key in d1[k]:
                if key in d2[k]:
                    new_d[key] = sum(d1[k][key]) + sum(d2[k][key])

    return new_d



combine2(d1, d2)

'''
create a file birthdays.py that will do the following:

(a) write a function that reads birthdays of people
    from the user and stores them in a dictionary
    of dictionaries.  Once the user enters 'stop', you 
    will read no more input from the user.  You may
    assume the user will give valid input.

    Sample Input:
    month day name: February 23 Bob
    month day name: May 3 Katie
    month day name: May 8 Paul
    month day name: May 8 Lucy
    month day name: stop

    Sample Ouput (i.e. returned by function)
    { 'February': {'23': ['Bob']},
    'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} }
'''
def birthday():
    bday_d = {}
    while True:
        birthdate = input('month day name (''stop'' to quit):')
        if birthdate == 'stop':
            break
        else:
            birthdate = birthdate.split()
            month, day, name = birthdate[0], birthdate[1], birthdate[2]
            if month in bday_d:
                if day in bday_d[month]:
                    bday_d[month][day].append(name)
                else:
                    bday_d[month][day] = [name]
            else:
                bday_d[month] = {day : [name]}
    print(bday_d)

'''
(b) Write a function called mostCovered that will take 
the dictionary entered by the user in part (a) and
return the month that has the most number of 
birthdays
'''
def mostCovered(bday_d):
    current_best = ['None', 0]
    for month in bday_d:
        sum_dates = 0
        for day in bday_d[month]:
            sum_dates += len(bday_d[month][day])
        if current_best[1] < sum_dates:
            current_best = [month, sum_dates]
    print(current_best[0])
    return current_best




'''
(c) write a function called invert() that will take
the birthday month dictionary entered by the user in
part(a) and return the equivalent brithday dictionary

Sample Input is the dictionary returned in part (a)

Sample Output:
{'Bob': ('February', '23'), 
'Katie': ('May', '3'),
'Paul': ('May', '8'), 
'Lucy': ('May', '8')}
'''

def invert(d):
    invert_d = {}
    for month in d:
        for day in d[month]:
            for person in d[month][day]:
                invert_d[person] = (month, day)
    print(invert_d)
    return invert_d

#invert({ 'February': {'23': ['Bob']}, 'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} })