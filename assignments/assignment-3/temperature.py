#2443227
#Sara ISabella Barajas-Cruz

# toCelsius
def toCelsius():
    f = int(input('Temperature in fahrenheit:'))
    c = (f - 32)*(5/9)
    return round( c, 1)

'''
Download the file data.txt from Moodle. In your main
program, open the file data.txt for reading only. From this file you are to read all the lines
from the year 1964 to 1975 into a dictionary temp_dict. That is, all the lines in your file
before 1964 should not appear in temp_dict dictionary. In temp_dict the keys are the
years (as an integer), and the values are the list of temperatures from JAN to DEC (as floats and
changed to Celsius).
HINT: the map function may be useful to do fast change of floats from strings and from
Fahrenheit to Celsius.
3.
'''
temp_dict = {}
input_file = open('data.txt', 'r')


# for lines in input_file:
#     lines = lines.readlines().split()
#     print(lines)
#     if lines[0][0:3] == '19':

#         year = lines[0]
#         temp_lst = lines[1:]

#         for i in temp_lst:
#             list = map(toCelsius(), temp_lst)
#             temp_dict[year] = list
# print(temp_dict)
# DOESNT RUN
input_file.close()
'''
(time estimate: 10 minutes) Write a function called avgTempYear that takes two arguments: a
dictionary (of same format as you read from the data.txt file) and year. The function returns
the average temperature for the given year in the dictionary rounded to 2 decimal places. If the
provided year is not in the dictionary, your code should use exceptions to handle it as we have
done in class by using the try-except-else block as needed. In the case of invalid year,
you should print a friendly message and your function in such a case should return nothing.
'''
    
# def avgTempYear(d, year):
#     try:
#         for keys in d: 
#             d.get(year)
#     except None:
#         print('This year isn\'t in the dictionnary')
#     else:
#         average = sum(d[year]) / len(d[year])
#         return round(average, 1)
'''(time estimate: 10 minutes) Write a function topThreeYears that takes a dictionary (of
same format as you read from the data.txt file) and returns a list of the three largest averages
in descending order among all the years. Pay attention to what data structures you may use for
efficiency.
5. (time estimate: 15 minutes) Write a function called avgTempMonth that takes a dictionary (of
same format as you read from the data.txt file) and a month (as a string of 3 characters) and
returns the average temperature for the given month across all years rounded to 2 decimal places.
Note that you may create a dictionary in your function to help you go back and forth between
string and integer representation of months.
For example: month_dict = {‘JAN’: 1, ‘FEB’: 2, ‘MAR’: 3, etc.}
'''
# qst 4
# def topThreeYears(d, lst):
#     list = []
#     for key in d:
#         list.append(avgTempYear(d, year))
#     for i in list:
#         if list[i] < list[i+1]:
#             list[i], list[i+1] = list[i+1], list[i]
#     lst = list[:4]
#     return lst
#DOESNT RUN
    
'''
# # qst 5
# def avgTempMonth(d, month):
#     month_dict = {}
#     months = ['JAN', 'FEB',	'MAR',	'APR',	'MAY',	'JUN',	'JUL',	'AUG',	'SEP',	'OCT',	'NOV',	'DEC']
#     for year in d:


#     d[month] = 

#DOESNT RUN
'''
