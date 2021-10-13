class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int: # Brute Force
        time = 0
        for point in range(0, len(points)-1):
            current = [points[point][0], points[point][1]]
            dest = [points[point+1][0], points[point+1][1]]
            while current[0] != dest[0] and current[1] != dest[1]: #Diagonal
                if current[0] < dest[0]:
                    current[0] += 1
                else:
                    current[0] -= 1
                if current[1] < dest[1]:
                    current[1] += 1
                else:
                    current[1] -= 1
                time += 1
                
            while current[0] != dest[0]: # Horizontal
                if current[0] < dest[0]:
                    current[0] += 1
                else:
                    current[0] -= 1
                time += 1
                    
            while current[1] != dest[1]: # Vertical
                if current[1] < dest[1]:
                    current[1] += 1
                else:
                    current[1] -= 1
                time += 1
                
        return time
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for idx in range(0, len(points)-1):
            start = points[idx]
            end = points[idx+1]
            time += max(abs(start[0]-end[0]), abs(start[1] - end[1]))
        return time
