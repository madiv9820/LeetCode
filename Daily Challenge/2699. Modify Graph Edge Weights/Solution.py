from typing import List
from collections import defaultdict
import heapq

class Solution:
    def modifiedGraphEdges(self, 
                           n: int, 
                           edges: List[List[int]], 
                           source: int, 
                           destination: int, 
                           target: int) -> List[List[int]] :
        INF = 2e9   # Infinity value
        # Creating adjacency list
        adjacency_List = defaultdict(dict)

        for src, dest, dist in edges:
            # We are including those values which have
            # +ve distances.
            if dist != -1:
                adjacency_List[src][dest] = dist
                adjacency_List[dest][src] = dist

        # Djikstra's Algorithm to find the shortest path from one node to another`
        def djikstras_Algorithm(source: int, destination: int) -> int:
            # Calculating minimum distance from source to each node
            distance_From_Source = defaultdict(int)
            # Currently, taking minimum distance of each node to be infinity
            for node in range(n): distance_From_Source[node] = INF
            # Distance from source to source = 0
            distance_From_Source[source] = 0

            visited = [False] * n   # Keeping track of nodes visited
            
            # Using priority queue to get minimum distance
            min_Heap = [(0, source)]
            heapq.heapify(min_Heap)

            while min_Heap:
                dist, node = heapq.heappop(min_Heap)
                visited[node] = True

                for neighbour in adjacency_List[node]:
                    if (distance_From_Source[neighbour] > 
                            dist + adjacency_List[node][neighbour]):
                        '''
                            Since it is given distance can be negative, as of now
                            we are taking them as +ve, so that we can find minimum
                            distance
                        '''
                        distance_From_Source[neighbour] = dist + adjacency_List[node][neighbour]

                        if not visited[neighbour]:
                            heapq.heappush(min_Heap, (distance_From_Source[neighbour], neighbour))
            
            return distance_From_Source[destination]     # Returning distances

        '''
            Checking if we have already a path shorter than target,
            Returning an empty list because we cannot be change anything
        '''
        distance_From_Source = djikstras_Algorithm(source, destination)
        if distance_From_Source < target: return []     
        
        '''
            Checking if we get distance from source to
            destination equal to target, then we can mark
            all the negative distance as infinite, because
            we already have required distance
        '''
        equal_To_Target = distance_From_Source == target

        for index in range(len(edges)):
            src = edges[index][0]
            dest = edges[index][1]
            dist = edges[index][2]
            
            '''
                Now we will add the nodes which have -ve distances,
                one by one to the graph.
            '''
            if dist == -1:
                # If we already have required distance, 
                # will mark -ve's as INF else
                dist = INF if equal_To_Target else 1    
                adjacency_List[src][dest] = dist    # Adding node to the adjacency list
                adjacency_List[dest][src] = dist    # Adding node to the adjaceny list
                edges[index][2] = dist      # Updating the distance in edges

                if not equal_To_Target:
                    '''
                        If distance from source to target is not equal to the target,
                        we will again find the shortest distance from source, destination
                        but this time, we have added a new node.
                    '''
                    new_Distance = djikstras_Algorithm(source, destination)
                    if new_Distance <= target:
                        equal_To_Target = True
                        edges[index][2] += target - new_Distance 

        return edges if equal_To_Target else []    # returning modified edges

if __name__ == '__main__':
    # n = int(input('Enter no of nodes: '))
    # edges = []
    # wanna_Continue = True

    # print('Enter edges: ')
    # while wanna_Continue:
    #     src, dest, dist = map(int, input().split())
    #     edges.append([src, dest, dist])

    #     wanna_Continue = (True if input('Wanna Continue (y/n): ') == 'y' else False)
    
    # source = int(input('Enter Source:'))
    # destination = int(input('Enter Destination: '))
    # target = int(input('Enter target: '))

    test_cases = [ {'n': 5, 'edges': [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]],
                    'source': 0, 'destination': 1, 'target': 5 },
                    {'n': 3, 'edges': [[0,1,-1],[0,2,5]],
                    'source': 0, 'destination': 2, 'target': 6},
                    {'n': 4, 'edges': [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]],
                        'source': 0, 'destination': 2, 'target': 6}
                ]
    
    for test_case in test_cases:
        sol = Solution()
        modifiedEdges = sol.modifiedGraphEdges(test_case['n'], 
                                               test_case['edges'], test_case['source'], 
                                               test_case['destination'], 
                                               test_case['target'])
    
        print(modifiedEdges)