class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        consecutive = 0
        for num in nums:
            consecutive = 0 if num == 0 else consecutive + 1 
            if consecutive > max_ones:
                max_ones = consecutive
        return max_ones