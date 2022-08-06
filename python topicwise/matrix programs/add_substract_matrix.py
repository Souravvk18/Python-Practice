#substracting two matrix.

# a = [[6,3],[4,5]]
# b= [[5,6],[7,8]]
# c=[[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         c[i][j] = a[i][j] - b[i][j]

# print(c)

# o/p- [[1, -3], [-3, -3]]



# adding two matrices

a = [[6,3],[4,5]]
b= [[5,6],[7,8]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        c[i][j] = a[i][j] + b[i][j]

print(c)

# o/p- [[11, 9], [11, 13]]

