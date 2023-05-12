# Write a function that takes an unknown number of arguments and returns their sum.
# Write a function that takes two arguments, the first being a string and the second 
# being an unknown number of integers. The function should return a new string where the
# integers have been added to the original string.


def sum_nums(*numberz):
    sum=0
    for num in numberz:
        sum+=num
    return sum
print(sum_nums(1,2,3,4,5))


# Write a function that takes an unknown number of keyword arguments and returns a dictionary 
# where the keys are the argument names and the values are the argument values.


def add_integers_to_strings(strs,*integers):
    result =strs
    for int in integers:
        result+=strs(int)
        return result
print(add_integers_to_strings("The sum of the intergers: ",3,4,5,7,9))


# Write a function that takes a function and an unknown number of arguments, and returns the result
# of calling the function with the arguments.

def numbers_function(func,*args):
    return func(*args)
print(numbers_function(2,3,4,9))

# Write a function that takes a list of integers and an unknown number of keyword arguments. The function
# should return a new list where each integer in the original list has been multiplied by the value of 
# the corresponding keyword argument.

def multiply(numbers,**kwargs):
    nums = []
    for i in numbers:
        if i < len(kwargs):
            nums.append()
        else:
            nums.append()


# Write a function that takes a list of integers and an unknown number of additional integers as
# arguments. The function should return the index of the first occurrence of the sum of the list 
# and the additional integers

def first_sum(numbs,*args):
    total = sum(numbs) + sum(args)
    return numbs.index(total)


# Write a function that takes an unknown number of keyword arguments, each with a string value. The 
# function should concatenate all the strings and return the resulting string.

def concat_string(**kwargs):
    return ''.join(kwargs)