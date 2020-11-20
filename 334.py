'''
This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.
'''

def generate_all_possiblity(a,b):
    print(a, ' -----', b)
    try:
        if a % b == 0 and a >=b:
            return [a+b, a-b, a *b, int(a/b) ]
        elif b % a == 0 and b > a:
            return [a + b, b-a, a * b, int(b / a)]
        elif a >= b :
            return [a + b, a - b, a * b]
        else:
            return [a + b, b - a, a * b]
    except ZeroDivisionError:
        pass

def func(array):
    result1 = generate_all_possiblity(array[0], array[1])
    # print(result1)
    for res1 in result1:
        result2 = generate_all_possiblity(res1, array[2])
        for res2 in result2:
            res3 = generate_all_possiblity(res2, array[3])
            if res3:
                if 24 in res3:
                    return True
    else:
        return False

print(func([5,2,7,8]))
