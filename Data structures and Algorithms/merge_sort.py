def merge_sort(list):
    """
    sort a list in ascending order , return a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    conquer: recursively sort the sublist created in previous step
    combine: merge the sorted sublists created in previous step

    overall sorting process takes O(n log n) time.
    """
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right= merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    divide the unsorted list at midpoint into sublists
    returns two sublists - left and right
    
    takes overall O(log n) time.
    """

    mid = len(list)//2
    left = list[: mid]
    right =list[mid :]

    return left, right

def merge(left, right):
    """
    merges two lists(arrays), sorting them in the process
    return a new merge list
    
    runs in overall O(n) time
    """

    l=[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+= 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l
def verify_sorted(list):
    n= len(list)

    if n== 0 or n==1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

alist= [11, 33, 22, 55,44, 66, 88, 77]
l=merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
print(l)


"""
False
True
[11, 22, 33, 44, 55, 66, 77, 88]
"""