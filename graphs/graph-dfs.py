class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v, u):
        # if graph at node v is empty fill with list with node u
        if self.graph.get(v) == None:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)

    def __str__(self):
        return f"{self.graph}"

    def dfs(self, start):
        # declare empty set of visited nodes
        visited = set()

        # declare queue
        s = []

        # enqueue start node initially and add
        # start node to visited set as well
        s.append(start)
        visited.add(start)

        # loop until stack is empty
        while s != []:
            # dequeue first node of queue
            node = s.pop()
            print(node)

            # see what neighbors of current node are
            for neighbor in self.graph[node]:

                # if neighbors of curretn node are not yet visited
                # enqueue them and add them to visited in advance 
                # now even though they have not been explicitly "visited" yet
                if neighbor not in visited:
                    s.append(neighbor)
                    visited.add(neighbor)

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "A")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "B")
    graph.add_edge("C", "D")
    graph.add_edge("D", "B")
    graph.add_edge("D", "C")
    graph.add_edge("E", "B")

    graph.dfs("A")
    print(graph)


            
