from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculating total chalk used in one cycle
        total_Chalk = sum(chalk)
        # Calculating k left after completing n cycles
        # k_left = k - n * total_Chalk = k % total_Chalk
        # n = k // total_Chalk
        k_left = k % total_Chalk
        
        # Now iterating through each chalk
        for i in range(len(chalk)):
            if chalk[i] > k_left: return i
            k_left -= chalk[i]

        # Our cycle has been completed, now k = 0
        return 0    # Returning first index