'''given email adresses of them are unqiue 

INPUT SPECFIcCATION:
--> first line of input is integer n: designating number of email adresses to read
--> the next n lines are n adresses'
after the @ letter number dots 
after @ cant be 

SAMPLE INPUT:
foo@bar.com
f0.o+
'''
def clean(address):
    '''
    address is a string email address 
    return cleaned adress
    '''

    # remove everything between + and @
    plus_index = address.find('+')
    #find dunction returns -1 if not found 
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:address[plus_index]] + address[at_index:]
    
    # remove all dots
    address = address.replace('.', '')
    
    #for char in range(at_index):

    #everything lowercase
    address = address.lower()

    return address

n = int(input())
valid_addys = []
#valid_addys = set()
for emails in range(n):
    address = input()
    address = clean(address)
    if address not in valid_addys: 
        valid_addys.append(address)
#valid_addys.add(adress)

print(len(valid_addys))

