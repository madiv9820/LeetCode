from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self,
                        n: int, 
                        edges: List[List[int]], 
                        succProb: List[float], 
                        start_node: int,
                        end_node: int) -> float:
        
        # Creating Adjacency List
        adjacency_List = defaultdict(dict)
        for index in range(len(edges)):
            src, dest, prob = edges[index][0], edges[index][1], succProb[index]
            adjacency_List[src][dest] = prob
            adjacency_List[dest][src] = prob

        # Djisktra's Algorithm To Find Minimum Distance
        # Between Any Two Nodes
        def djikstras_algorithm(source: int, destination: int) -> float:
            # Since djikstra's algorithm require a min Heap for
            # finding minimum distance from one node to another
            # but we need maximum probability, so we will use a
            # max heap 

            '''
                In max heap, we are providing 2 values, first value
                is probability of current node from source, since our
                current node is source, hence probability is 1. Since
                heaps in python are min by default, so in order to create
                max heap we are negating the values, and second value is 
                current node.
            '''
            max_Heap = [(-1, source)]     
            heapq.heapify(max_Heap)
            
            visited = [False] * n   # Keep a check of nodes which are already visited
            probability = [0] * n   # Probability of reaching to node from the source
            probability[source] = 1

            # Traversing through each node
            while max_Heap:
                prob, node = heapq.heappop(max_Heap)    # Popping node which has maximum probability
                prob = -prob   # Making it +ve

                visited[node] = True    # Marking visited of current node as True
                
                # Updating probabilities of 
                # neighbors of the current node
                for neighbor in adjacency_List[node]:
                    if probability[neighbor] < (prob * adjacency_List[node][neighbor]):
                        probability[neighbor] = (prob * adjacency_List[node][neighbor])

                        if not visited[neighbor]:
                            heapq.heappush(max_Heap, (-probability[neighbor], neighbor))

            # Returning maximum probability 
            # of reaching source to destination
            return probability[destination]
        
        return djikstras_algorithm(start_node, end_node)    # Return maximum probability