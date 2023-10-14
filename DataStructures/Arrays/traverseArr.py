from array import *

arr1 = array('i' , [1,2,3,4,5,6])
arr2 = array('d' , [1.2, 3.4, 5.6])


def traverseArray(array):
    for i in range(len(array)):     ##O(n)
        print(array[i])

traverseArray(arr1)

