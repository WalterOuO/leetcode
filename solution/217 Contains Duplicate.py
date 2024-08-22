def containsDuplicate(self, nums: List[int]) -> bool:
      # book = {}
      # for num in nums:
      #     if num not in book:
      #         book[num] = 1
      #     else:
      #         book[num] += 1
      # return set(book.values()) != {1}
          
      seen = set()
      for num in nums:
          if num in seen:
              return True
          seen.add(num)
      return False
