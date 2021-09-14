# Transpose a matrix in Python

#using numpy..

# import numpy
# matrix = [[1,2,3],[4,5,6]]

# print(numpy.transpose(matrix))

"""
[[1 4]
 [2 5]
 [3 6]]
 """


#  using zip

matrix=[(1,2,3), (4,5,6),(7,8,9)]

# for row in matrix:
#     print(row)

t_matrix = zip(*matrix)

for row in t_matrix:
    print(row)

"""
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)
"""