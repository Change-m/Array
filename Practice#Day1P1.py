class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = int(high - low)
        if low % 2 == 1 or high % 2 == 1:
            return int(1 + res/2)
        return int(res/2)# count odd number in the between two numbers range
