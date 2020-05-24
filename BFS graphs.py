from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph :

    # Constructor
    def __init__(self) :
        # default dictionary to store graph
        self.graph = defaultdict (list)

        # function to add an edge to graph

    def addEdge(self, u, v) :
        self.graph[u].append (v)


    def BFS(self, start):
        ans = []
        visted = [False]*len(self.graph)

        queue = []
        queue.append(start)
        visted[start] = True

        while queue:

            val = queue.pop(0)
            ans.append(val)

            for i in self.graph[val]:
                if visted[i] == False:
                    queue.append(i)
                    visted[i] = True
        print(ans)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)



