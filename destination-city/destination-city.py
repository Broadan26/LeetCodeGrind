class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set(path[0] for path in paths)
        end = set(path[1] for path in paths)
        return end.difference(start).pop()