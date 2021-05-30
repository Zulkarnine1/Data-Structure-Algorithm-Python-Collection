# A recursive function calls itself in the function body

# This is an example of an recursive function, however it is a bad recursive function as it deosn't
# any base case it will keep calling itself resulting in stackoverflow

def inception1():
    inception1()

# inception1()


# A recursive function should have 3 important features:
# 1. The recursive case - the case for which the function should call itself again.
# 2. The base case - the case for which the function should end and return the result
# 3. The returns - the function should have a return for both the cases.

# Exercise 1 - Find the error
"""
The following function has an error. The function is supposed to return True when counter is greater than 3,
but it seem to be returning 'None'. Can you figure the error?
"""

counter = 0
def inception2():
    global counter
    if counter > 3:
        return True
    else:
        counter+=1
        print(counter)
        inception2()

# out = inception2()
# print(out)

# Exercise 1 - Solution
"""
Everything with the recursive function was okay but one. It wasn't returning for the recursive case. 
This is a reference to the 3rd feature where it states both cases should ahve return. 
"""

counter = 0
def inception3():
    global counter
    if counter > 3:
        return True
    else:
        counter+=1
        print(counter)
        # This is where the error was
        return inception3()

# out = inception3()
# print(out)


# Exercise 2 - Define a find factorial function with recursion and iteration
# Solution :

def find_fact_recursion(x):
    if x == 0:
        return 0
    if x >= 1:
        return 1
    else:
        return x * find_fact_recursion(x-1)

# print(find_fact_recursion(0))



def find_fact_iter(x):
    if x == 0:
        return 0
    ans = 1
    while(x >= 1):
        ans = ans * x
        x-=1
    return ans

# print(find_fact_iter(10))



# Exercise 3 - Given a number N return the index value of the Fibonacci sequence, where the sequence is:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3
#
# For example: fibonacciRecursive(6) should return 8

# Solution

# O(2^N)
def fibonacciRecursive(x):
    if x < 2 :
        return x
    return fibonacciRecursive(x-1) + fibonacciRecursive(x-2)

# 3 -> 2,1
# 2 -> 1,0 ---- 1 -> 1

print(fibonacciRecursive(4))
def fibonacciIterative(x):
    arr = [0,1]
    for i in range(2,x+1,1):
        arr.append(arr[i-2]+arr[i-1])
    return arr[x]

print(fibonacciIterative(8))


# Exercise : Implement functions that reverses a string with recursion and iteration

# Solution :

def reverse_string_rec(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string_rec(s[1:]) + s[0]

print(reverse_string_rec("abcd efgh"))


def reverse_string_iter(s):
    if len(s)<=1:
        return s
    else:
        res = ""
        for i in range(len(s)-1,-1,-1):
            res += s[i]
        return res

print(reverse_string_iter("abcd efgh"))
