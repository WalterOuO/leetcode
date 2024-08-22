class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # # 雙重迴圈暴力解
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        
        # 用字自動回找index，引入 j = target - i
        # for i in nums:             # [3,2,4]  target = 6
        #     j = target - i
        #     if j in nums and nums.index(i) != nums.index(j):   # [3,3]例子會讓nums.index(i)=nums.index(j)=0
        #         return [nums.index(i), nums.index(j)]
        
        # for i in nums:
        #     j = target - i
        #     if j in nums:
        #         if i == j and nums.count(i) == 2:
        #             return [nums.index(i), nums.index(i, nums.index(i)+1)]
        #         elif i != j:   
        #             return [nums.index(i), nums.index(j)]

        
        # list
        hashlist = []
        for i in range(len(nums)):      # i為 index，x是 value
            x = target - nums[i]        # nums[i] = 7 , x = 2, [7,]
            if nums[i] in hashlist:
                return [nums.index(x), i]
            else:
                hashlist.append(x)      # 沒看過就存進去，第二次看到裡面有就代表裡外一致
