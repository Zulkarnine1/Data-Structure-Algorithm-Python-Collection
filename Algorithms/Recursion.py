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

# Exercise
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

# Exercise - Solution
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

out = inception3()
print(out)