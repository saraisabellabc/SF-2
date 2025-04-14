from __future__ import annotations
from functools import total_ordering 

@total_ordering

class Account:
    def __init__(self, gold):
        '''create Account with value gold'''
        self.gold = gold

    def addGold(self, amount: int) -> None:
        '''add gold amount to this Account'''
        self.gold = 0

    def doubleGold(self) -> None:
        '''doubling gold amount in Account'''
        self.gold = self.gold * 2

    def __lt__(self, other:Account) -> bool:
        '''return True if Account and other are of the same type and gold 
        of Account is less than gold of other'''
        return isinstance(other, Account) and \
            self.gold < other.gold
    def __eq__(self, other:Account) -> bool:
        ''' are equal'''
        return isinstance(other, Account) and \
            self.gold == other.gold
# main program
a1 = Account(500)
a2 = Account(500)
a3 = Account(56)
a4 = Account(34)

print('a4 <? a3', a4 < a3)
print('a1 ==? a4', a1 == a4)

# implementing == and < or > , it can infer the rest 

print('a4 > a1', a4 > a1)
print('a1 != a4', a1 != a4)



