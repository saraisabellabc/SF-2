
def isdistinct(year:int) -> bool:
    s = str(year)
    digits_used = []
    
    for char in s:
        if char in digits_used:
            return False
        digits_used.append(char)
    return True


year = int(input())
year = year + 1

while not isdistinct(year):
    year = year + 1

print(year)