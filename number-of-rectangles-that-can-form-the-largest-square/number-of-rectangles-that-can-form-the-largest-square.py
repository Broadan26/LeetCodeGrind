class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        max_length = 0
        for rect in rectangles: # Check each rectangle
            max_side = min(rect[0], rect[1]) # Determine biggest square
            if max_length == max_side: # Increment if already seen
                count += 1
            elif max_side > max_length: # Change if new max
                count = 1
                max_length = max_side
        return count