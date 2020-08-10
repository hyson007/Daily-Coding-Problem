import itertools

def selec_index(index_lst, lst):
    each_result = []
    for index, value in zip(index_lst, lst):
        if index != '0':
            each_result += [value]
    return each_result

def return_binary(lst):
    return [ selec_index(i, lst) for i in itertools.product('01', repeat=len(lst))]

#print(selec_index(('0', '1', '1'), [1,2,3]))

print(return_binary([1 , 2 ,3]))
