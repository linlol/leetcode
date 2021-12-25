class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #sliding window?
        ones = []
        for i,j in enumerate(boxes):
            if j == '1':
                ones.append(i)
        left, right = 0, len(ones) #record the number of balls stay on LHS or equal/ RHS the current position
        ini, ini_val = 0, sum(ones)
        ans = []
        while ini < len(boxes):
            if ini == 0:
                ans.append(ini_val)
            else:
                ini_val += left
                ini_val -= right
                ans.append(ini_val)
            if boxes[ini] == '1':
                left += 1
                right -= 1
            ini += 1
        return ans
