def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx+1, len(input_list)):
            if input_list[min_idx]>input_list[j]:
                min_idx=j

        input_list[idx],input_list[min_idx]=input_list[min_idx],input_list[idx]
list = [19,2,71,45,40,11,91,27]
selection_sort(list)
print(list)

"""[2, 11, 19, 27, 40, 45, 71, 91]"""



def selection_sort(list):
    for i in range(len(list)):
        min_i = i
        for j in range(i+1, len(list)):
            if list[min_i]>list[j]:
                min_i=j

        list[i],list[min_i]=list[min_i],list[i]
list = [50, 20, 30, 10, 60, 80, 40]
selection_sort(list)
print(list)

"""[10, 20, 30, 40, 50, 60, 80]"""