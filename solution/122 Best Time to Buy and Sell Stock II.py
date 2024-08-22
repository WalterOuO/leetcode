def maxProfit(self, prices: List[int]) -> int:
      '''
      概念是兩個for
      第一個for迭代每組後的數字i
      第二個for去找i後面有沒有比他大的數字j，再持續往後比較，直到沒有比較大的
          就更新參數j為最大的那個，並算出profit，並把profit儲存起來
      '''
      small = prices[0]
      prof = 0
      for i in prices:
          if i < small:
              small = i
          elif i - small > 0:
              prof += i - small
              small = i
      return prof

      '''
      profit = 0
      for i in range(1, len(prices)): # +1 --> no need to keep same day buy and sell
              profit+= max(0, prices[i] - prices[i-1])

      return profit     
      '''
