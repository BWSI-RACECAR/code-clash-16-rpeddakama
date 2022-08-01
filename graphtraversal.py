"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #16 - Graph Traversal (graphtraversal.py)


Author: Chris Lai

Difficulty Level: 10/10

Prompt: Before the Grand Prix, every contestant is given a map of different obstacles that are in the course. 
The goal of the course is to reach the finish line as fast as possible while traveling through the obstacles. 
A sample of the map, which is a directed acyclic graph, is shown below.

Given a dictionary “graph” object containing information about the nodes and edges of each obstacle and their 
transitions, find the shortest path from the start node to the finish line and return the time it takes to 
travel through that path.

Test Cases:

Input:
{ 'Start': {'Invisible Maze': 15, 'The Labyrinth': 20}, 
'Invisible Maze': {'Park Walk': 45}, 
'Ice Valley': {'Tower of Doom': 45, 'Sloped Madness': 85}, 
'The Labyrinth': {'Ice Valley': 45, 'Sloped Madness': 155}, 
'Tower of Doom': {'Cone Slalom': 10, 'Ice Valley': 45}, 
'Park Walk': {'Tower of Doom': 45}, 
'Cone Slalom': {'Sloped Madness': 15, 'Street Dodge': 30}, 
'Street Dodge': {'Finish': 70}, 
'Sloped Madness': {'Finish': 60}, 'Finish': {}}

Start -> Invisible Maze -> Park Walk -> Tower of Doom -> Cone Slalom -> Sloped Madness -> Finish 

Output: 190


Constraints:
- The distance "d" will always span the range 0 <= d <= 10^5
- The number of nodes "n" in the provided graph will always span the range 0 <= n <= 10^2
- The number of connecting obstacles "k", or adjacent nodes, will always span the range 0 <= n <= 2
- Provided dictionaries will always have the starting node at the beginning of the data structure and the ending node at the end of the data structure
- The start node will always be named "Start" and the final node will always be named "Finish"

"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max_val][1]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


class Solution:
    global locations
    global graph
    locations = {}
    graph = [[] for r in range(1000)]

    def dijkstra(self):
        global graph
        global locations
        n = len(locations)
        cost = [1e7] * n
        visited = [False] * n

        cost[0] = 0
        queue = PriorityQueue()
        queue.insert((0, 0))

        while not queue.isEmpty():
            top = queue.delete()
            node, dist = top

            for i in range(len(graph[node])):
                cur = graph[node][i]
                # print("CUR", cur)
                if dist + cur[1] < cost[cur[0]]:
                    cost[cur[0]] = dist + cur[1]
                    queue.insert((cur[0], cost[cur[0]]))

        return cost[locations["Finish"]]

    def spath_algo(self, dict):
        global locations
        # type graph: dict
        # return type: int (shortest path as an int)

        cnt = 0
        for i in dict:
            locations[i] = cnt
            cnt += 1

        if "Finish" not in locations.keys():
            locations["Finish"] = len(locations)

        for i in dict:
            for j in dict[i]:
                graph[locations[i]].append((locations[j], dict[i][j]))
                # print(graph[locations[i]])

        return self.dijkstra()


def main():
    tc1 = Solution()

    graph = {}
    nodes = input().split(",")
    nodes[len(nodes) - 1] = nodes[len(nodes) - 1].strip()
    for i in range(0, len(nodes) - 1):
        graph[nodes[i]] = {}
        edges = input().split(",")
        edges[len(edges) - 1] = edges[len(edges) - 1].strip()
        weights = input().split(" ")
        for j in range(0, len(edges)):
            graph[nodes[i]][edges[j]] = int(weights[j])

    shortest_distance = tc1.spath_algo(graph)

    # graph = {
    #     "Start": {"Invisible Maze": 15, "The Labyrinth": 20},
    #     "Invisible Maze": {"Park Walk": 45},
    #     "Ice Valley": {"Tower of Doom": 45, "Sloped Madness": 85},
    #     "The Labyrinth": {"Ice Valley": 45, "Sloped Madness": 155},
    #     "Tower of Doom": {"Cone Slalom": 10, "Ice Valley": 45},
    #     "Park Walk": {"Tower of Doom": 45},
    #     "Cone Slalom": {"Sloped Madness": 15, "Street Dodge": 30},
    #     "Street Dodge": {"Finish": 70},
    #     "Sloped Madness": {"Finish": 60},
    #     "Finish": {},
    # }
    # shortest_distance = tc1.spath_algo(graph)

    print(shortest_distance)


if __name__ == "__main__":
    main()
