'''
COCI'06  Regional #1 Bard
every evening vilalgers in a small village gather around a big fire
and sing songs 

a prominent member of the community is the bard. every evening, if the bard is present, he sings a brand new song that no villager has heard before,
and no there song is sung that night . in the event that the bard is not present, other 
villagers sing without him and exchange all songs thT THE KNOW (NOTE: villagers can only learn a new song from the bard)

Given the list of villagers present for E consecutive evenings, output all villagers that know all songs sung during hat period.
INPUT SPECIFICATIONS:


Sample input 1:
4
3
2 1 2
3 2 3 4
3 4 2 1

two ppl
just the barn sings 
numbers are villegers names 
Sample output 1:
1
2
4

sample input-2:
8
5 
4 1 3 5 4
2 5 6
3 6 7 8
2 6 2
5 2 6 8 1 

sample output-2 :
1
2
6 
8

sample input 3:

'''
input = input().split()
n = input[0]
e = input[1]
