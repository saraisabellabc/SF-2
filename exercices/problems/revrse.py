'''num = input()

s = '' 
for i in range(len(num)):
    s = num[i] + s'''

# num = int(input())
# i = 10 
# while i < num:
#     x = num % i
#     i *= 10
#     print(x)

num = int(input())  # Input the number
reversed_num = 0

while num > 0:
    # Extract the last digit
    last_digit = num % 10
    
    # Append the last digit to the reversed number
    reversed_num = reversed_num * 10 + last_digit
    
    # Remove the last digit from the original number
    num //= 10

print(reversed_num)