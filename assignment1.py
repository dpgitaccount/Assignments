# Q1. Write a Python program to determine the largest among three numbers entered by the user.

# User input
num1 = float(input("Enter the first number is: "))
num2 = float(input("Enter the second number is: "))
num3 = float(input("Enter the third number is:  "))

## Conditional statements
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# printing of largest number
print("The largest number is ", largest)

# Q2. Question Write a Python program to check if a given year is a leap year.
# Check if the year is divisible by 4
# Check if the year is divisible by 100, but not divisible by 400
# If the year satisfies either of the above conditions, it's a leap year

def CheckLeapYear(year):
    # check year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100, but not divisible by 400
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    else:
        return False
# User input
year = int(input("Enter the year: "))

if CheckLeapYear(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year")
    
# Question 3:
# Write a Python program to print the following pattern:1,22,333,4444,55555

n = 5
for i in range(1, n+1):
    print()
    for j in range(1, i+1):
        print(i, end=' ')

# Question 4:
# Write a Python program to print the following pattern: left to right *,**,***,****,*****

n = 5
for i in range(1, n+1):
    print()
    for j in range(1, i+1):
        print("*", end=' ')
    
        
# Question 5:
# Write a Python program to print the following pattern: right to left *,**,***,****,*****

n = 5
for i in range(1, n+1):
        print(" " * (n - i) + "*" * i)
        


# Question 6:
# Write a program that prints the numbers 1 to 100. However, for multiples of 3, print "Fizz" instead of the
# number. For multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

start = int(input("enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(1, 100+1):
    ## Conditional Statements
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Q7. Write a Python program to find the sum of all prime numbers up to n.

# taking an input of the number from the user
last_number = int(input("Enter the last number up till which sum of prime number is to be found:"))
sum = 0
# Initializing the sum to 0
for number in range(2, last_number + 1):
#  starting from 2 as it is the first prime number.
    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;
# Only if the number is a prime number, continue to add it.
    if i is not number:
        sum = sum + number
print("The sum of prime numbers from 1 to ", last_number, " is :", sum)

# Question 8:
# Write a Python program to print the Fibonacci sequence up to n terms. The Fibonacci series is a sequence of
# numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# 0,1,1,2,3,5,8,13,21,34

def fib(n):
    a = 0
    b = 1
    if n<0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        return b
print(fib(10))

# Question 9:
# Write a Python program to print the following pattern:
def print_full_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

rows = int(input("Enter the number of rows for the full pyramid: "))
print("Full Pyramid:")
print_full_pyramid(rows)

# Question 10:
# Write a Python program to print the following pattern: A,BB,CCCCC,DDDDDDD,EEEEEEEEE
def print_tingle_pyramid(rows):
    for i in range(rows):
        char = chr(ord('A') + i)  
        print(char * (i * 2 + 1))  
rows = 5
print("Tingle Pyramid:")
print_tingle_pyramid(rows)



