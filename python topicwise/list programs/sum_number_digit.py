list = [15,25,35,45]
list = [35,25,75,85]
res= []

for ele in list:
    sum = 0

    for digit in str(ele):
        sum += int(digit)

    res.append(sum)
print("the integer sum:", res)


# o/p- the integer sum:[6, 7, 8, 9]
# the integer sum: [8, 7, 12, 13]