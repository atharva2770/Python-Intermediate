from array import *

arr1 = array('i', [1,2,3,4,5,6])

def searchInArr(array,value):
    for i in array:     #O(n)
        if i == value:
            return array.index(value)

    return "The element does not exist"

print(searchInArr(arr1, 5))
print(searchInArr(arr1, 15))


# x = list(map(int, input("Enter multiple values: "). split()))
# print("List of students: ", x)