'''
This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the
specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

'''
#
def func(array, k):
    if sum(array) < k:
        return False
    for item1 in array:
        for item2 in array:
            if item2 == item1:
                continue
            for item3 in array:
                if item3 == item2 or item3 == item1:
                    continue
                # print(item1, item2, item3)
                if sum([item1, item2, item3]) == k:
                    return True
    return False

print(func([20, 303, 3, 4, 25], 49))