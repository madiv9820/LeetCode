from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_Size = 0
        n = len(nums)
        
        # Find the maximum element in nums (this will be the maximum possible bitwise AND value)
        max_val = max(nums)

        for start in range(n):
            bitwise_And = ~0  # Initialize to all 1's so it doesn't interfere with the AND operation
            for end in range(start, n):
                # Perform bitwise AND progressively
                bitwise_And &= nums[end]
                
                # Check if the current AND equals the max possible value
                if bitwise_And == max_val:
                    max_Size = max(max_Size, end - start + 1)

        return max_Size