class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Creating a map, all the alphabets with their positions
        alpahbet_map = {chr(ord('a')+i):str(i+1) for i in range(26)}
        # Converting s to its respective numeric string
        nums = "".join(alpahbet_map[ch] for ch in s)
        
        # Transforming nums to its sum of its digits
        nums = int(nums)        
        # while k > 0 and nums > 9:
        #     temp = nums; nums = 0
        #     while temp > 0:
        #         nums += (temp % 10)
        #         temp //= 10
        #     k -= 1

        for i in range(k):
            if nums < 10: break
            nums = sum(int(digit) for digit in str(nums))

        return nums     # Returning nums