from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = []  # This will store the XOR results for each query
        
        # Initialize the prefix XOR array where prefix_XOR_Sum[i] will hold the XOR of elements from 0 to i
        # The idea is to use the cumulative XOR to quickly compute the XOR for any subarray
        prefix_XOR_Sum = [0] * len(arr)
        prefix_XOR_Sum[0] = arr[0]  # The first element is just the first element of arr
        
        # Build the prefix XOR array
        for index in range(1, len(arr)):
            # Each prefix_XOR_Sum[i] holds the XOR of all elements from arr[0] to arr[i]
            prefix_XOR_Sum[index] = prefix_XOR_Sum[index - 1] ^ arr[index]
        
        # Now process each query in the queries list
        for start, end in queries:
            # If the start of the query is 0, the XOR from 0 to 'end' is simply prefix_XOR_Sum[end]
            # Because prefix_XOR_Sum[end] already contains the XOR of elements from arr[0] to arr[end]
            if start == 0: 
                res = prefix_XOR_Sum[end]
            else:
                # Otherwise, we need the XOR from 'start' to 'end'
                # We use the property of XOR: 
                # prefix_XOR_Sum[end] gives the XOR from arr[0] to arr[end]
                # prefix_XOR_Sum[start-1] gives the XOR from arr[0] to arr[start-1]
                # XORing them together cancels out the first part and leaves us with the XOR from arr[start] to arr[end]
                res = prefix_XOR_Sum[end] ^ prefix_XOR_Sum[start - 1]
            
            # Append the result for this query to the result list
            xor.append(res)

        # Finally, return the list of results for all queries
        return xor

    
if __name__ == '__main__':
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]
    sol = Solution()
    print(sol.xorQueries(arr, queries))