pos = -1

def search(list, n):

    #  i = 0
    #
    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         #print('found')
    #         return True
    #     i+=1
    #
    # return False
    #
    for i,num in enumerate(list):
        if num == n:
            globals()['pos'] = i
            #print('found')
            return True

    return False


list = [5,6,8,9,3,2]
n = 9

if search(list, n):
    print("Found at " ,pos+1)
else:
    print("Not Found")