class Solution:
    def twoSum(self, nums, target: int):
        list1=[]
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list1.append(i)
                    list1.append(j)
                    return list1

x=Solution()
print(x.twoSum([5,5],10))
