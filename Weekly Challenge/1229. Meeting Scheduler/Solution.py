from typing import List

class Solution:
    def minAvailableDuration(self, 
                                slots1: List[List[int]], 
                                slots2: List[List[int]], 
                                duration: int) -> List[int]:
        # Sort the slots by their start times
        slots1.sort(); slots2.sort()

        # Using pointers to traverse both lists of slots
        index1, index2 = 0, 0

        # Traverse both lists of slots
        while index1 < len(slots1) and index2 < len(slots2):
            s1, e1 = slots1[index1]
            s2, e2 = slots2[index2]

            # Find the overlap between the two slots
            start = max(s1, s2)
            end = min(e1, e2)

            # Check if the overlap is enough for the required duration
            if end - start >= duration: return [start, start + duration]

            # Move the pointer that has the earlier end time
            if e1 < e2: index1 += 1
            else: index2 += 1

        # If no suitable slot found, return an empty list
        return []