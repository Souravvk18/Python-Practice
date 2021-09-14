arr =[5,2,3,4,6]

mul= 1
n= 7
for i in arr:
    mul= mul*(i % n)

print("the remaining is:", mul %n)

# method -2---

def remaining(arr, l,n):
    mul =1
    for i in arr:
        mul = mul * (i % n)
    print("the remaining is:",mul % n)
arr = [2,3,4,5]
l= len(arr)
n=11
remaining(arr,l,n)

# the remaining is: 10

