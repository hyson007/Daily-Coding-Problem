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
