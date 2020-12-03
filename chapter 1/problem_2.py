class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for num in nums:
            evens += 1 if len(str(num)) % 2 == 0 else 0
        return evens