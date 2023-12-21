from queue import Queue


class Graph:
    def __init__(self, n_v):
        self.n_v = n_v
        # graph will be n_v x n_v
        self.graph = [[0 for i in range(n_v)] for j in range(n_v)]

    def add_edge(self, v, u):
        # given nodes v and u connect node v to node u
        # by inserting 1 at the position [v][u]
        self.graph[v][u] = 1

    def __str__(self):
        return f'{[row for row in self.graph]}'

    def bfs(self, start):
        # declare empty set of visited nodes
        visited = set()

        # declare queue
        q = Queue()

        # enqueue start node initially and add
        # start node to visited set as well
        q.put(start)
        visited.add(start)

        # loop until queue is empty
        while not q.empty():
            # dequeue first node of queue
            node = q.get()
            print(node)

            # see what neighbors of current node are
            for i in range(self.n_v):

                # if neighbors of curretn node are not yet visited
                # enqueue them and add them to visited in advance 
                # now even though they have not been explicitly "visited" yet
                if (self.graph[node][i] == 1) and (i not in visited):
                    q.put(i)
                    visited.add(i)


if __name__ == "__main__":
    # declare number of vertices and edges
    n_v = 5

    # define graphs edges
    graph = Graph(n_v=n_v)
    graph.add_edge(0, 1)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(4, 1)

    # start traversal
    graph.bfs(0)
    print(graph)



            
