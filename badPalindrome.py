def isPalindrome(lst):
    '''
    determine if lst is a palindrome 
    :param lst: lst is a lst
    :return :True if lst is a palindrome; False otherwise
    '''
    temp = lst[:] #debug : [:] copying 
    temp.reverse() #debug : ()
    print(temp, lst)
    return temp == lst

def silly(n):
    '''
    gets nn inputs from uswrm Print ;yes if the sequenxe of inputs forms a palindrime; 'no' otherwise
    :param n: n is an integer > 0
    :return :None 

    '''
    result = []
    for i in range(n):
        elem = input('enter element:')
        result.append(elem)
    print(result)
    if isPalindrome(result):
        print('Yes')
    else:
        print('No')

silly(2)