
nums = [5,3,8,1,9,4,2,6]

def sort(nums):

    for i in range(7):
        minpos = i
        for j in range(i,8):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

sort(nums)

print(nums)
