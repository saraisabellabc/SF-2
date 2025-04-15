def combine2(d1, d2):
    '''
    >>> combine2({'a' :{ 3: [2], 4: [5,6]}}, {'a': {3:[8, 12]}})
    {3: 22}
    '''

d1 = {'a' :{ 3: [2], 4: [5,6]}, 'b': {6: [2, 7, 9], 4 : [5, 6]}}
d2 = {'a': {3:[8, 12]}, 'b':{7:[7, 33]}}


def combine2(d1, d2):
    result = {}
    for key in d1:
        if key in d2:
            for x in d1[key]:
                if x in d2[key]:
                    # lst1 = d1[key][x]
                    # lst2 = d2[key][x]
                    result[x] = sum(d1[key][x]) + sum(d2[key][x])
    return result 

print(combine2({'a' :{ 3: [2], 4: [5,6]}}, {'a': {3:[8, 12]}}))