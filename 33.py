my_list =  [2, 1, 5, 7, 2, 0, 5]

def func(my_list):
    i=1
    while i<= len(my_list):

        cur_list = sorted(my_list[:i])
        if len(cur_list) % 2 ==0:
            mid_pos_1 = len(cur_list)//2
            mid_pos_2 = len(cur_list)//2 - 1
            sum = cur_list[mid_pos_1] + cur_list[mid_pos_2]
            if sum % 2 ==0 :
                print(sum//2)
            else:
                print(sum/2)
        else:
            mid_pos = len(cur_list) // 2
            print(cur_list[mid_pos])
        i +=1

func(my_list)
