#2443227
#Sara Isabella Barajas-Cruz

def toCelsius(f):
    return round( (f - 32) * (5/9), 2)

def avgTempYear(d, year):
    try:
        average = sum(d[year]) / len(d[year])
    except KeyError :
        print('This year isn\'t in the dictionnary')
    else:  
        return round(average, 2)

def topThreeYears(d):
    top_3 = [-997,-998,-999]
    for year in d:
        average_temp = avgTempYear(d, year)    
        if average_temp > top_3[0]:
            top_3[2] = top_3[1]
            top_3[1] = top_3[0]
            top_3[0] = average_temp

        elif average_temp > top_3[1]:
            top_3[2] = top_3[1]
            top_3[1] = average_temp

        elif average_temp > top_3[2]:
            top_3[2] = average_temp

    return top_3

def avgTempMonth(d, month):
    month = month.upper()
    month_dict = {'JAN': 0, 'FEB': 1, 'MAR': 2, 'APR': 3, 'MAY': 4, 'JUN': 5, 'JUL': 6, 'AUG': 7, 'SEP': 8, 'OCT': 9, 'NOV': 10, 'DEC': 11}
    month_index = month_dict[month]
    
    total = 0 
    n_years = len(d)
    for year in d:
        total += d[year][month_index]
    return round(total / n_years, 2)


def belowFreezing(d):
    freezing_months = set()
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    for year in d:
        temps = d[year]
        i = 0
        while i < len(temps):
            if temps[i] < 0:
                freezing_months.add(months[i])
            i += 1

    return freezing_months

                

# MAIN PROGRAM
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

output_file = open('data_celsius.txt', 'w')
input_file = open('data.txt', 'r')
for line in input_file:
    lines = line.split()
    if not lines or not lines[0].isdigit():
        output_file.write(line)

for year in temp_dict:
    output_file.write(f"{year}   ")
    for value in temp_dict[year]:
        output_file.write(f"{value}   ")
    output_file.write("\n")







    
