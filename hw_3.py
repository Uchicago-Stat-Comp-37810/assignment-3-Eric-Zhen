# Name: Zhen Dai
# hw3.py
import math
import random

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(m,n):
    if n == 0:
        return("zero cannot be a divisor.")
    else:
        a = (m % n == 0)
        return a

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?

# ********** Exercise 2 ********** 

# Define not_equal function here
def not_equal(m,n):
    a = not (m==n)
    return a

# Test cases for not_equal
print not_equal(1,1)  #This should return False.
print not_equal(1,2)  #This should return True.
print not_equal(3,3)  #This should return False.
print not_equal(4,2)  #This should return True.
print not_equal(5,5)  #This should return False.
print not_equal(7,6)  #This should return True.
print not_equal(121,121)  #This should return False.
print not_equal(111,22)  #This should return True.

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    d = a*b + c
    return d

## Test for multadd
print multadd(1,1,1) #This should return 2
print multadd(1,2,1) #This should return 3
print multadd(2,2,1) #This should return 5

## 2 - Equations
pie = math.pi
angle_test = multadd(0.5, math.cos(pie/4), math.sin(pie/4))

def ceiling(x):
    if x == int(x):
        return x
    else:
        y = int(x) + 1
        return y
    
ceiling_test = multadd(2.0, math.log(12,7), ceiling(276.0/19.0))


# Test Cases
angle_test = multadd(0.5, math.cos(pie/4), math.sin(pie/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(2.0, math.log(12,7), ceiling(276.0/19.0))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    a = random.randint(0,100)
    print(a)
    b = (a%3 == 0)
    return b

# Test Cases
for i in range(20):
    a = rand_divis_3()
    print a
    
#In each of the 20 cases, the first number printed is divisible by 3 if and only if the second boolean value printed is True.

c = 0
for i in range(3000):
    c += rand_divis_3()
print(c)

#The last number printed should be close to 1000 justified by the law of large number.

