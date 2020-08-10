'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

'''

my_string = 'AAAABBBCCDAA'

def convert(my_string):
    output =''
    i = 0
    while i <len(my_string)-1:
        cur_string = my_string[i]
        repeated_times = 1

        while cur_string == my_string[i+repeated_times]:
            repeated_times += 1
            if i+repeated_times == len(my_string):
                break
        output += cur_string + str(repeated_times)
        i += repeated_times
    return output

print(convert(my_string))
