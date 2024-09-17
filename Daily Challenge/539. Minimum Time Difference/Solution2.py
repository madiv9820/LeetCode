from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Helper function to convert time in "HH:MM" format to minutes
        def convertTimeToMinutes(time_stamp: str) -> int:
            hours, minutes = map(int, time_stamp.split(':'))
            return 60 * hours + minutes

        # Array to keep track of all possible time points in a 24-hour period
        timeExists = [False] * (24 * 60)
        # Initialize to the maximum possible minute count (1440)
        earliestTimeStamp = 24 * 60
        # Initialize to the minimum possible minute count 
        latestTimeStamp = 0  

        # Process each time point in the list
        for time_stamp in timePoints:
            # Convert current time point to minutes
            stampInMinutes = convertTimeToMinutes(time_stamp)
            
            # If the time point already exists, 
            # return 0 as the minimum difference
            # because there are two identical time points
            if timeExists[stampInMinutes]:
                return 0
            
            # Mark this time point as exists
            timeExists[stampInMinutes] = True

            # Update the earliest and latest time stamps encountered
            earliestTimeStamp = min(earliestTimeStamp, stampInMinutes)
            latestTimeStamp = max(latestTimeStamp, stampInMinutes)

        # Calculate the initial minimum difference 
        # considering the circular nature of the clock
        minDifference = (24 * 60 - latestTimeStamp + earliestTimeStamp)

        # Variable to store the previous time point in the iteration
        previousStamp = earliestTimeStamp
        
        # Iterate through the minute markers to find the minimum difference
        for currentStamp in range(earliestTimeStamp + 1, len(timeExists)):
            # If there is a time point at the current minute
            if timeExists[currentStamp]:
                # Calculate the difference between the current and previous time points
                difference = currentStamp - previousStamp
                # Update the minimum difference if a smaller difference is found
                minDifference = min(minDifference, difference)
                # Update the previous time stamp to the current one
                previousStamp = currentStamp

        return minDifference