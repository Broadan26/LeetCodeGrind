class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        extend_bed = [0] + flowerbed + [0] # Makes it harder to run off ends of list
        for idx in range(1, len(extend_bed)-1):
            if extend_bed[idx] == extend_bed[idx-1] == extend_bed[idx+1] == 0:
                extend_bed[idx] = 1
                n -= 1
            if n <= 0: return True
        return n == 0
            