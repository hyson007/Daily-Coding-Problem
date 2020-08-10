'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

from queue import LifoQueue

open_paren = ['(', '{', '[']
close_paren = [')', '}', ']']

q = LifoQueue()
my_string = "([])[]({})"
my_string1 = "([)]"
my_string2 = "((()"

def check_pair(a,b):
    if a+b == '()' or a+b == ')(':
        return True
    elif a+b == '[]' or a+b == '][':
        return True
    elif a+b == '{}' or a+b == '}{':
        return True
    else:
        return False


def check_balance(my_string):
    for s in my_string:
        if s in open_paren:
            q.put(s)

        elif s in close_paren:
            cur_output = q.get()
            if not check_pair(s, cur_output):
                return False
    if q.empty():
        return True
    return False

print(check_balance(my_string))
print(check_balance(my_string1))
print(check_balance(my_string2))



