class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        distances = []
        for (x, y) in points:
            distance = -(x * x + y * y)
            if len(distances) == k:
                heapq.heappushpop(distances, [distance, x, y])
            else:
                heapq.heappush(distances, [distance, x, y])
        return [[x,y] for [distance, x, y] in distances]