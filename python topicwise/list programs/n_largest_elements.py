

def maxelements(list1, N):
    finallist=[]

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1= list1[j]
    
        list1.remove(max1)
        finallist.append(max1)
    return finallist

list1= [10, 20, 50, 60, 30, 40, 70]
N= 3

print("largest numbers are", maxelements(list1, N))

"""largest numbers are [70, 60, 50]"""