'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

my_array = [(30, 75), (0, 50), (60, 150)]

def number_in_tuple(num, my_tuple):
    return num in range(my_tuple[0], my_tuple[1]+1)

def check_overlapping(*args):
    room_needed = 0
    for index, arg in enumerate(args):
        start_time = arg[0]
        end_time = arg[1]
        for rest_list in args[index+1:]:
            if number_in_tuple(start_time, rest_list) or number_in_tuple(end_time, rest_list):
                room_needed +=1
    return room_needed

print(check_overlapping(*my_array))
