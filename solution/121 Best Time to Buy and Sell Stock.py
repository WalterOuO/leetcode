def maxProfit(self, prices: List[int]) -> int:
      # 選一天買入，選一天賣出
      # Input: array prices = [1day, 2day,.......]
      # Output: Return最大收益，後面都比較便宜就Return 0
      # 價格(相對)最低點、(絕對)最大收益
      small = prices[0]
      prof = 0
      for i in prices:
          if i < small:
              small = i
          elif i - small > prof:          # 牛逼在這裡，else if的條件不只是if的反面意思，也可以假設為其他if
              prof = i - small
      return prof

      # [ 3 2 6 5 0 3 ]
      # lis = []
      # small = min(prices)
      # i = len(prices)
      # while i > 0:
      #     if i == 1:
      #         return 0
      #     elif small == prices[len(prices)-1]:
      #         prices.pop()
      #         small = min(prices)
      #     else:
      #         break 
      #     i -= 1
      # for k in range(prices.index(small)+1,len(prices)):
      #     lis.append(prices[k])
      # big = max(lis)
      # return big-small
