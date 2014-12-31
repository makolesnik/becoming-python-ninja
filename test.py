# http://gsl.mit.edu/media/programs/ghana-summer-2011/materials/lab10.pdf

import itertools
from random import randint

"""
1. Find (9362323892^2983232639)%132. Only use 1 line of code. 
"""

print pow(9362323892, 2983232639, 132)


"""
2. Write a function printNinja(inp) that will print “You’re a Ninja!” if inp is inp is less than 100
and greater than 80, and “You have been attacked by a Ninja!” if inp is any other value.
Only use 2 lines of code.
"""
def printNinjA(inp):
    result = "You`re a Ninja!" if (inp in range (81, 100)) else "You have been attacked by a Ninja!"; return result

"""
3. X=[1,2,3,4,5,6,7,8]. Write a slice operator or pair of slice operators that will return
[7,5,3,1]. Only use one line of code. X=[1,2,3,4,5,6,7,8]. Write a slice operator or pair of slice operators that will return
[7,5,3,1]
"""
print [x for x in [1,2,3,4,5,6,7,8] if x % 2]

"""
4. Using List comprehensions (one line each):
a. Print an array with the square of all numbers in the range (1:10)a
"""
print [x**x for x in range(1, 11)]

"""
b. Print an array of all even numbers in range(5369:5421)
"""
print [x for x in range(5369, 5421) if not x % 2]
       
"""
c. You roll two dice that are represented by the list: [1,2,3,4,5,6]. Return an array of
tuples with all possible combinations. For this problem, (1,6) and (6,1) are
different outputs. 
"""

g = lambda a:  list(itertools.permutations(a,2))+ zip(a,a); print g([1,2,3,4,5,6])

"""
d. Copy your code from C, and modify it so that values are only added to the output
list if their product is greater than 9. (3,4) should be outputted, but (3,3) should
not. 
"""
print [(k,j) for i, (k,j) in enumerate(list(itertools.permutations([1,2,3,4,5,6],2))+ zip([1,2,3,4,5,6],[1,2,3,4,5,6])) if k*j > 9 ]
    
"""
5. Write a generator to print the sum of all 2^n, where n is in between 1 and 10000.If your
computer crashes, you did it wrong. Use one line. 
"""
print 2**randint(1,10000)


"""
6. Write a filter (using a lambda function) to find all even numbers greater than 100   in
range(80,120). Use one line. 
"""
print filter( lambda x: x % 2 == 0 and x > 100, range(80,120))


# Yes, I am ashamed of the code, but I am learning how to write it better





