class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        
        return max_profit


"""
want to maximize profit
so buy lowest, sell highest
if no such possibility exists
return 0 (keep max profit 0)

two pointers?
elements in the input prices array represent prices at a time
so need to find best time slot or interval
therefore, sliding window?
start l and r pointers at opposite ends of array so can search space efficiently once?
may not need to
(is sorting not an option?), if sorted, then would make more sense to 
if sorting, could hash orig index to sorted index

while l < r

if l higher than r, 
l += 1

elif l == r
if l+1 > r-1
l += 1
else r -= 1

else
r -= 1

or dynamic programming

T: O(N) at least? O(N^2) maybe?
S: O(1) if comparing with pointers in-place, O(N) if creating new data container

"""