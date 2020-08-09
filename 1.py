'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def func(my_list, k):
    for i in my_list:
        copy_list = [i for i in my_list]
        copy_list.remove(i)
        if k-i in copy_list:
            return True
    return False

print(func([10, 15, 3, 7, 8], 14))

