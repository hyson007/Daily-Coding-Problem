'''
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''



pre_process_list = [-9, -2, 0, 2, 3]

def process_list(my_list):
    return sorted([ i *i for i in my_list])

print(process_list(pre_process_list))
