def bsearch(list, idx0, idxn, val):

    if (idxn<idx0):
        return None
    else:
        midval = idx0+((idxn-idx0)//2)

    if list[midval] >val:
        return bsearch(list, midval +1, idxn, val)
    elif list[midval] < val:
        return bsearch(list, midval+1, idxn, val)
    else:
        return midval
list = [8,11,24, 30, 50, 56]
print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0,5, 100))

"""
2
None
"""
