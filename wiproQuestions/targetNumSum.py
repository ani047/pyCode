def target_sum(nums,target):
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            sum = nums[i]+nums[j]
            if sum==target:
                return i,j

arr = [2,3,6,3,7]
trg=9
tuple = target_sum(arr,trg)
print(tuple)
