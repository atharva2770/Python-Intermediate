
pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2      ##Integer Division

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False

list = [5,6,8,9,3,2,50,25,66,15]
n = 10

if search(list, n):
    print("Found at " ,pos+1)
else:
    print("Not Found")