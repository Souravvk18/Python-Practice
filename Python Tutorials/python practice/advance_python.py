
# MULTITHREADING

'''
for a given list of numbers print square and cube of every numbers.
'''

#simple method

# def calc_square(numbers):
#     print("calculate square of numbers")
#     for n in numbers:
#         print('square:', n*n)
#
# def calc_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         print('cube:', n*n*n)


# arr= [2,3,5,6,7]
# calc_square(arr)
# calc_cube(arr)

'''o/p-

square: 4
square: 9
square: 25
square: 36
square: 49
calculate cube of numbers
cube: 8
cube: 27
cube: 125
cube: 216
cube: 343
'''

# another method

# import threading
#
# def calc_square(numbers):
#     print("calculate square of numbers:\n")
#     for n in numbers:
#         print('square:',n*n)
#
# def calc_cube(numbers):
#     print("calculate cube of numbers:\n")
#     for n in numbers:
#         print('cube:',n*n*n)
#
# arr = [2,3,5,6,8]
#
# t1= threading.Thread(target=calc_square, args=(arr,))
# t2= threading.Thread(target=calc_cube, args=(arr,))
#
# t1.start()
# t2.start()

'''o/p- 
calculate square of numbers:

square: 4
square: 9
square: 25
square: 36
square: 64
calculate cube of numbers:

cube: 8
cube: 27
cube: 125
cube: 216
cube: 512

'''
# import multiprocessing
#
# def calc_square(numbers):
#     print("calculate square of numbers:")
#     for n in numbers:
#         print('square:'+ str(n*n))
#
# def calc_cube(numbers):
#     print("calculate cube of numbers:")
#     for n in numbers:
#         print('cube:'+ str(n*n*n))
#
# if __name__=="__main__":
#     arr = [5,7,8,9]
    # p1= multiprocessing.Process(target=calc_square, args=(arr,))
    # p2=multiprocessing.Process(target=calc_cube, args=(arr,))
    #
    # p1.start()
    # p2.start()

'''o/p- 
calculate cube of numbers:
square:25
square:49
square:64
square:81
calculate cube of numbers:
cube:125
cube:343
cube:512
cube:729
'''

# import multiprocessing
#
# result=[]
#
# def calc_square(numbers):
#     global result
#     print("calculate square of numbers:")
#     for n in numbers:
#         print('square:'+ str(n*n))
#         result.append(n*n)
#     print('within a process:'+ str(result))
#
# if __name__=="__main__":
#     arr = [5,7,8,9]
#     p1= multiprocessing.Process(target=calc_square, args=(arr,))
#     p1.start()
#
#     print('outside a process:' + str(result))

'''o/p- 
calculate square of numbers:
square:25
square:49
square:64
square:81
within a process, result:[25, 49, 64, 81]
'''

# ** Sharing data between processes using arrays and value.

import multiprocessing

def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx]= n*n

if __name__=="__main__":
    numbers=[3,4,5,9]
    result=multiprocessing.Array('i',4)
    p=multiprocessing.Process(target=calc_square, args=(numbers,result))

    # p.start()
    # p.join()
    # print(result[:])

# o/p-  [9, 16, 25, 81]

#** sharing data between processes using Queue.

import multiprocessing

def calc_square(numbers,q):
    for n in (numbers):
        q.put(n*n)

if __name__=="__main__":
    numbers=[3,4,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

'''o/p-
9
16
25
'''






