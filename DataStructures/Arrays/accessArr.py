from array import *

arr1 = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print("Aree bhava mothi value takli ki punha kar")
    else:
        print(array[index])     ##O(1)

accessElement(arr1, 5)

# accessElement(arr1, 7)