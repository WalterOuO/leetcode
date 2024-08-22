def removeDuplicates(self, nums: List[int]) -> int:
      # return len(list(set(nums)))
      # dic = {}
      # for i in nums:
      #     if i in dic:
      #         dic[i] += 1
      #     else:
      #         dic[i] = 1
      # return len(list(dic.keys()))
  
      k = 0
      for i in range(len(nums)):
          if nums[i] != nums[k]:
              nums[k+1] = nums[i]
              k += 1
      return k + 1
