class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        import heapq # Convert the list to a heap
        heapq.heapify(nums)
        
        big1, big2 = heapq.nlargest(2, nums) # Collect 2 largest
        small1, small2 = heapq.nsmallest(2, nums) # Collect 2 smallest
        
        return (big1 * big2) - (small1 * small2) # Return product diff