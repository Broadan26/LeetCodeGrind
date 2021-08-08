class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        Finds all the paths from the source node (0) to the end node (len(graphs)-1)
        Returns a list of all paths
        '''
        paths = []
        self.search(graph, [0], paths)
        return paths
    
    def search(self, graph: list[list[int]], start: int, paths: list[list[int]]):
        '''
        Performs DFS to find list of paths
        '''
        if start[-1] == len(graph) - 1:
            paths.append(start)
            return
        for path in graph[start[-1]]:
            self.search(graph, start+[path], paths)