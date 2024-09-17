from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sort the list of time points in ascending order
        timePoints.sort()

        # Helper function to convert time in "HH:MM" format to minutes
        def convertTimeToMinutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return 60 * hours + minutes

        # Calculate the initial minimum difference as the difference
        # between the first and last times in the sorted list, 
        # accounting for the circular nature of the clock (24-hour format)
        minDifference = (
            24 * 60 - 
            convertTimeToMinutes(timePoints[-1]) + 
            convertTimeToMinutes(timePoints[0])
        )

        # Iterate through the sorted list to find the minimum difference
        for i in range(len(timePoints) - 1):
            # If minDifference is zero, return immediately 
            # since it's the smallest possible difference
            if minDifference == 0:
                return 0
            
            # Convert the current and previous times to minutes
            currentTimeInMinutes = convertTimeToMinutes(timePoints[i + 1])
            previousTimeInMinutes = convertTimeToMinutes(timePoints[i])

            # Calculate the difference between consecutive times
            minDifference = min(minDifference, 
                                    currentTimeInMinutes - previousTimeInMinutes)

        return minDifference
