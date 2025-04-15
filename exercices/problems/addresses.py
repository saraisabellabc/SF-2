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
    at_index = address.find('@')

    if plus_index != -1 and plus_index < at_index:
        address = address[:plus_index] + address[at_index:]
    
    # remove all dots
    local, domain = address.split('@')
    local = local.replace('.', '')

    
    #for char in range(at_index):

    #everything lowercase
    address = local + '@' + domain.lower()

    return address

n = int(input())
# valid_addys = []
valid_addys = set()
for emails in range(n):
    address = input()
    clean_address = clean(address)
    valid_addys.add(clean_address)
    # if address not in valid_addys: 
    #     valid_addys.append(address)
#valid_addys.add(adress)

print(valid_addys)

