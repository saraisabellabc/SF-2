def combine(d1, d2):
    '''
    return a new dictionary where each key is a key that is both in d1 and d2 and the value associated with each key in the new dictionary is the sum of all the intergers in the lists.
    '''
    new_dict = {}
    for key in d1:
        if key in d2: # its the same key
            lst_d1 = d1[key] # gives 5, 6
            lst_d2 =  d2[key] # gives 8
            new_dict[key] = sum(lst_d1 + lst_d2)

    return new_dict

d1 = {1: [2], 4: [5, 6]}
d2 = {4: [8]}