def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i]==target:
            return i
    return None
def verify(index):
    if index is not None:
        print("target found at index:", index)
    else:
        print("target not found in list")
    
number=[1,2,3,4,5,6,7,8,9,10]
result=linear_search(number, 7)
verify(result)

result=linear_search(number, 15)
verify(result)

"""
o/p-
target found at index: 6
target not found in list
"""


def search(list1,key):
    for i in range(len(list1)):
        if key ==list1[i]:
            print("key element is found at index:", i)
            break
    else:
        print("element is not found")
list1 = [10, 40, 20, 30, 50, 70, 60, 100]
# print(list1)

#taking user input 

# key =int(input("enter the key element:")) 
# search(list1, key)

""" enter the key element:60
key element is found at index: 6"""

# key  =50
# search(list1, key)

"""[10, 40, 20, 30, 50, 70, 60, 100]
key element is found at index: 4"""

def search (list1, key):
    list2 = []
    flag = False
    for i in range(len(list1)):
        if key ==list1[i]:
            flag = True
            list2.append(i)
    if flag==True:
        print("key element is found at index: ")
        for i in list2:
            print(i)
    else:
        print("key is not found")

list1 =[30, 40, 20, 50, 100, 60, 20]
print(list1)
# key=int(input("enter the key element:"))
key = 50
search(list1, key)

""" 
normal input -
key element is found at index:
3

user input --
enter the key element:20
key element is found at index: 
2
6

enter the key element:100
key element is found at index: 
4
"""
