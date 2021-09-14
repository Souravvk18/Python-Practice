# program to add two matrix

X =[ [3,4,5],
     [4,5,6],
     [7,8,9]]

Y =[ [2,3,4],
     [5,6,7],
     [2,4,6]]

add =[ [0,0,0],
       [0,0,0],
       [0,0,0]]

#iterate through rows

for i in range(len(X)):

#iterate through columns
    for j in range(len(X[0])):
        add[i][j] = X[i][j] + Y[i][j]


print(add)

# for r in add:
#     print(r)

"""[[5, 7, 9], [9, 11, 13], [9, 12, 15]]

[5, 7, 9]
[9, 11, 13]
[9, 12, 15]

"""
