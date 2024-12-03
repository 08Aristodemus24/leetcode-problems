import queue

class Graph:
    def __init__(self, graph: dict) -> None:
        self.graph = graph

    def acyclicTraverseDepthFirst(self, src: str) -> None:
        stack = [src]

        while len(stack) > 0:
            current = stack.pop()
            print(current)

            for neighbor in self.graph[current]:
                stack.append(neighbor)

    def acyclicTraverseBreadthFirst(self, src: str) -> None:
        queue_1 = queue.Queue()
        queue_1.put(src)

        while not queue_1.empty():
            current = queue_1.get()
            print(current)

            for neighbor in self.graph[current]:
                queue_1.put(neighbor)

    def acyclicDFHasPath(self, src: str, dest: str) -> bool:
        return self._acyclicDFHasPath(self.graph, src, dest)

    def _acyclicDFHasPath(self, graph: dict, src: str, dest:str) -> bool:
        if src == dest:
            return True

        for neighbor in graph[src]:
            if self._acyclicDFHasPath(graph, neighbor, dest) == True:
                return True

        return False

    def acyclicBFHasPath(self, src: str, dest: str) -> bool:
        return self._acyclicBFHasPath(self.graph, src, dest)

    def _acyclicBFHasPath(self, graph: dict, src: str, dest: str) -> bool:
        queue_1 = queue.Queue()
        queue_1.put(src)

        while not queue_1.empty():
            current = queue_1.get()

            if current == dest:
                return True

            for neighbor in graph[current]:
                queue_1.put(neighbor)

        return False

    def acyclicShortestPath(self) -> None:
        pass



# keep list of visited  notes to cover cyclic graphs
# Create graph class from scratch with acyclic and cyclicDepthFirst, acyclic and cyclicBreadthFirst, acyclic and cyclicHasPath, shortestPath,
# Maybe the splution for avoiding an infinite loop in traversals is to keep a list of the visited nodes