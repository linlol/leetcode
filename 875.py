#simple binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            ans = 0
            for i in piles:
                if i % k == 0:
                    ans += i//k
                    continue
                ans += i//k + 1
            return ans
        low, high = 1, max(piles)
        mid = (low + high)//2
        while high - low > 1:
            time = helper(mid)
            if time > h:low = mid
            else:high = mid
            mid = (low + high)//2
        return low if helper(low) <= h else high
