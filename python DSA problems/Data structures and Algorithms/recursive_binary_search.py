def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    else:
        midpoint=(len(list))//2
    if list[midpoint]==target:
        return True
    else:
        if list[midpoint]<target:
            return recursive_binary_search(list[midpoint+1 :], target)
        else:
            return recursive_binary_search(list[: midpoint], target)
def verify(result):
    print("target found:", result)
number=[1,2,3,4,5,6,7,8]
result=recursive_binary_search(number, 7)
verify(result)

result=recursive_binary_search(number, 10)
verify(result)

'''
o/p-
target found: True 
target found: False
'''

