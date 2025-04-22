from __future__ import annotations
# import math

'''You are to create a Fraction Class that defines a rational number with common arithmetic operations

1) define a constructor where the default values (that is, if nothing provided by user) for the numerator
abd denominator are 0 and 1 respectively

in all other cases, make sure to check for the following:
--> if denominator is 0, raise ZeroDivisionError
--> if the numerator is 0, then the numerator and denominator attributes of the object are 0 and 1 respectively
--> determine the sign of the fraction and put it in the numerator
--> make sure you store the fraction in reduced form

2) define __add__ function that takes one argument other_fraction, adds tgis Fraction'''

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        
        if numerator == 0:
            self.denominator = 1
            self.numerator = 0
        
        if (numerator * denominator) < 0:
            sign = -1
        else:
            sign = 1
            
        # if denominator < 0 and numerator > 0:
        #     numerator = -numerator
        #     denominator = -denominator

        i = max(numerator, denominator)
        gcd = 1
        while i > 0:
            if numerator % i == 0 and denominator % i == 0:
                gcd = i
                break
            i -= 1
        self.numerator = abs(numerator) // gcd * sign
        self.denominator = abs(denominator) // gcd

        # greatest_c = math.gcd(numerator, denominator)
        # numerator = numerator // greatest_c
        # denominator = denominator // greatest_c

        # # if we work / change the inputs, we have to assign them to the attributes only at the end 
        # self.numerator = numerator
        # self.denominator = denominator
    def __repr__(self):
        return f'{self.numerator} / {self.denominator}'
    
    def __add__(self, other_fraction: Fraction ) -> Fraction :
        f_num = (self.numerator * other_fraction.numerator) + (other_fraction.numerator * self.denominator)
        f_denom = (self.denominator * other_fraction.denominator) 
        return Fraction(f_num + f_denom)
    
    def __sub__(self, other_fraction: Fraction) -> Fraction:
        f_num = (self.numerator * other_fraction.numerator) + (other_fraction.numerator * self.denominator)
        f_denom = (self.denominator * other_fraction.denominator)
        return Fraction(f_num - f_denom)
    
    # for != <= >= < > == we can only implement < > == which infer all the others
    def __eq__(self, other: Fraction) -> bool:
        return isinstance(other, Fraction) and (self.denominator * self.numerator == other.denominator * other.numerator) 
    
    def __ne__(self, other: Fraction) -> bool :
        return isinstance(other, Fraction) and (self.denominator * self.numerator != other.denominator * other.numerator) 
        # return not self.__eq__(other)
    
    def __gt__(self, other: Fraction) -> bool:
        return isinstance(other, Fraction) and (self.denominator * self.numerator > other.denominator * other.numerator) 
    
    def __ge__(self, other: Fraction):
        return isinstance(other, Fraction) and (self.denominator * self.numerator  >= other.denominator * other.numerator) 
    
        
    def __lt__(self, other: Fraction) -> bool:
        return isinstance(other, Fraction) and (self.denominator * self.numerator < other.denominator * other.numerator) 

    def __le__(self, other: Fraction) -> bool:
        return isinstance(other, Fraction) and (self.denominator * self.numerator <= other.denominator * other.numerator) 
    
    def float(self):
        # float representation of the function
        return round(self.numerator / self.denominator, 2)
    
    def sorted_fract(self, lst : list[Fraction]) -> list[Fraction]:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1

            while j >=0 and lst[j] < key:
                lst[j] = lst[j]
                j -= 1
            
            lst[j + 1] = key
        return lst




    
    

f1 = Fraction(1, 4)
f2 = Fraction(20, -4)
f3 = Fraction(5, 2)

# Example of sorting fractions using Insertion Sort
fractions_list = [f1, f2, f3]
sorted_fractions = f1.sorted_fract(fractions_list)
print("Sorted Fractions:", sorted_fractions)


#Main program 
f1 = Fraction(1, 4)
f2 = Fraction(20, -4)
print(f2.float())

