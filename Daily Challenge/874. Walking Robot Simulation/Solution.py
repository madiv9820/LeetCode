from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Creating a set of coordinates of obstacles
        # since it is possible to get same obstacles multiple times
        unique_Obstacles = {(x, y) for x, y in obstacles}

        # A dictionary to get the left(-2) 
        # and right(-1) of the particular direction
        left_Right_map = {
            "North": {-2: "West", -1: "East"},
            "South": {-2: "East", -1: "West"},
            "East": {-2: "North", -1: "South"},
            "West": {-2: "South", -1: "North"},
        }

        # A dictionary to tell how to move for a particular direction
        direction_map = {"North": (0, 1), "South": (0, -1), "East": (1, 0), "West": (-1, 0)}
        
        '''
        A lambda function to calculate the euclidean distance
        basically, its, (x1-x2)^2 + (y1-y2)^2
        Since, we need to calculate the distance from initial
        position, i.e. origin(0, 0), so we can simply take sum
        of squares of coordinates
        '''
        euclidean_Distance = lambda x,y: x**2 + y**2

        current_X, current_Y = 0, 0     # Current Position
        current_Direction = "North"     # Current Direction in which we have to move
        max_Distance = 0                # Max euclidean distance

        # Iterating through each command
        for command in commands:
            # Changing the direction of the robot
            if command == -2 or command == -1:
                current_Direction = left_Right_map[current_Direction][command]
            else:
                # Moving on the given path
                for _ in range(command):
                    next_X = current_X + direction_map[current_Direction][0]
                    next_Y = current_Y + direction_map[current_Direction][1]
                    
                    # Checking whether next position is obstical or not
                    if (next_X, next_Y) in unique_Obstacles: break

                    current_X, current_Y = next_X, next_Y   # Updating position
                    # Checking whether this coordinate 
                    # is farthest or not
                    max_Distance = max(max_Distance, 
                                        euclidean_Distance(current_X, current_Y))

        return max_Distance     # Returning max euclidean distance