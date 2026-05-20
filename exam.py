#1.Write a Python program to swap two variables a = 10 and b = 20 without using a third variable. Print both values before and after swapping.

a=10
b=20
print("before  swapping: ")
print("a= ",a)
print("a= ",a)
a,b=b,a

# print("after swapping:")
# print("a= ",a)
# print("a= ",a)

#Write a program that prints numbers from 1 to 30.
#  For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".


for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Grade Calculator Write a function get_grade(marks) that returns:
#"A" (≥80), "B" (≥65), "C" (≥50), "F" (below 50). Call it with at least 3 different values.

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(get_grade(92))   
print(get_grade(70))   
print(get_grade(55))   
print(get_grade(38))   



#Even Numbers Sum Using a for loop and range(),
#  calculate and print the sum of all even numbers from 1 to 100.

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)


#Factorial Function Write a function factorial(n) that returns the 
#factorial using a while loop. Test it with n=5 and n=0.

def factorial(n):
    if n < 0:
        return "Invalid: negative number"
    result = 1
    while n > 0:
        result *= n   # result = result × n
        n -= 1
    return result

# Test cases
print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")