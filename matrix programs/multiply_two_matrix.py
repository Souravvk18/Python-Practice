# program to multiply two matrices

x= [[2,3,4],
    [4,5,6],
    [3,6,9]]

y= [[1,3,5],
    [2,4,6],
    [3,5,7]]

multi = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#iterating by row of x
for i in range(len(x)):

    # iterating by column of y
    for j in range(len(y[0])):

        # iterating by row of y
        for k in range(len(y)):
            multi[i][j] += x[i][k] *y[k][j]

for m in multi:
    print(m)

""" o/p- 
[20, 38, 56]
[32, 62, 92]
[42, 78, 114]
"""

# x= [[2,3,4],
#     [4,5,6],
#     [3,6,9]]

# y= [[1,3,5],
#     [2,4,6,4],
#     [3,5,7],
#     [2,3,4,7]]

# print(len(y))
# print(len(x))
# print(len(y[3]))


