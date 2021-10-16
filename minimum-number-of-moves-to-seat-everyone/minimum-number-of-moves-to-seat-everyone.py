class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        swaps = 0
        for idx in range(len(seats)):
            swaps += abs(seats[idx] - students[idx])
        return swaps