#2443227
#Sara ISabella Barajas-Cruz

# question 1
def toCelsius(f):
    return round( (f - 32) * (5/9), 2)

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
# question 2
input_file = open('data.txt', 'r')

temp_dict = {}
for line in input_file:
    lines = line.split()

    if lines and lines[0].isdigit():
        year = int(lines[0])

        if 1964 <= year <= 1975:
            fahrenheit_temp = list(map(float, lines[1:]))
            celsius_temp = list(map(toCelsius, fahrenheit_temp))
            temp_dict[year] = celsius_temp

input_file.close()
'''
(time estimate: 10 minutes) Write a function called avgTempYear that takes two arguments: a
dictionary (of same format as you read from the data.txt file) and year. The function returns
the average temperature for the given year in the dictionary rounded to 2 decimal places. If the
provided year is not in the dictionary, your code should use exceptions to handle it as we have
done in class by using the try-except-else block as needed. In the case of invalid year,
you should print a friendly message and your function in such a case should return nothing.
'''
# question 3 
def avgTempYear(d, year):
    try:
        average = sum(d[year]) / len(d[year])
    except KeyError :
        print('This year isn\'t in the dictionnary')
    else:  
        return round(average, 2)

'''(time estimate: 10 minutes) Write a function topThreeYears that takes a dictionary (of
same format as you read from the data.txt file) and returns a list of the three largest averages
in descending order among all the years. Pay attention to what data structures you may use for
efficiency.

'''
# question 4


def topThreeYears(d):
    top_3 = [-1000,-1000,-1000]
    for year in d:
        average_temp = avgTempYear(d, year)    
        if average_temp > top_3[0]:
            top_3[0] = top_3[1]
            top_3[1] = top_3[2]
            top_3[0] = average_temp

        elif average_temp > top_3[1]:
            top_3[1] = top_3[0]
            top_3[1] = average_temp

        elif average_temp > top_3[2]:
            top_3[2] = average_temp

    return top_3

    
'''
5. (time estimate: 15 minutes) Write a function called avgTempMonth that takes a dictionary (of
same format as you read from the data.txt file) and a month (as a string of 3 characters) and
returns the average temperature for the given month across all years rounded to 2 decimal places.
Note that you may create a dictionary in your function to help you go back and forth between
string and integer representation of months.

'''
# question 5
def avgTempMonth(d, month):
    month = month.upper()
    month_dict = {'JAN': 0, 'FEB': 1, 'MAR': 2, 'APR': 3, 'MAY': 4, 'JUN': 5, 'JUL': 6, 'AUG': 7, 'SEP': 8, 'OCT': 9, 'NOV': 10, 'DEC': 11}
    month_index = month_dict[month]
    
    total = 0
    n_years = len(d)
    for year in d:
        total += d[year][month_index]
    return round(total / n_years, 2)
