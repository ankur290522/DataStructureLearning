from Stack import Stack

class DFSMaizeEmptyError(Exception):
    def __init__(self) -> None:
        self.errMessage = "The graph is empty"
        super().__init__(self.errMessage)
    
    def __str__(self) -> str:
        return f'CustomException: {self.errMessage}'

class DepthFirstSearch:
    def __init__(self, graph):
        if len(graph) == 0:
            raise DFSMaizeEmptyError
        self.graph = graph
        self.visited = [False] * len(graph)
        self.result = Stack()
        self._dfs(0)

    def _dfs(self, node):
        self.visited[node] = True
        self.result.push(node)
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor)

    def get_result(self):
        return self.result.read_elements_as_list()