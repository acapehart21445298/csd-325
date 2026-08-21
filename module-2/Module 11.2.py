# Arrington Capehart
# 8/1/2026
# Module 11.2 Assignment


number = int(input("Enter a positive integer: "))

# input validation here

while number <= 0:
    print("Please enter a positive integer greater than 0.")
    number = int(input("Enter a positive integer: "))
    
# This recursive function calls itself with a decreasing value of n
# until it reaches the base case of 0. Once the base case is reached,
# the function prints each number from 1 up to the original value of n.

def print_recursive(n):
    if n == 0:
        return
    
    print_recursive(n - 1)
    print(n)
    
print("Beginning Recursive Function")
print_recursive(number)
print("Ending Recursive Function")

# This non-recursive function prints numbers from 1 up to the value entered by the user.
# It uses a for loop to repeat the process instead of calling itself like the recursive function.
# The loop starts at 1 and continues until it reaches the value of n.

def print_non_recursive(n):
    for number in range(1, n + 1):
        print(number)
        
print()
print("Beginning Non-Recursive Function")
print_non_recursive(number)
print("Ending Non-Recursive Function")