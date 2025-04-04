'''
Consider cities and states in the US. Each state is given a two letter abbreviation. You are tasked to read n cities and states from the 
user and determine the number of special pairs.

Here is an example of a special pair:
SCRANTON PA and PARKER SC.
This is special pair since the first two characters of each city gives the abbreviation for the other city's state
That is, SC PA and PA SC.

A pair of cities is special if they meet this property and are not in the same state. your task is to determine the number of special 
pairs of cities in the provided input. Make sure your code is efficient. That is, make use of
efficient data structure

INPUT SPECIFICATION :
-- > first line is an integer n (n is large), the number of cities 
-- > next n lines: one per city. each line gives the name of a city in uppercase, a space, and its states abbeviation in uppercase.
NOte that the same city name can exist in multiple states but will not appear more than once in the same state.

OUTPUTspecification:
OUTPUT THE NUMBER OF special pairs of cities

sample input:
12
SCRANTON PA
MANISTEE MI
NASHUA NH
PARKER SC 
LAFAYETTE CO
WASHOUGAL WA
MYDDLEBOROUGH MA
COVINGTION LA
LAKEWOOD CO 

sample output:
9

- make it fast , no searching in a list 

read 5 different sample input from the user annd write this to a file, where there is an empty line between any two sample
inputs. Then from this file, read each sample input and determine (print) the number of special pairs of cities
'''