class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        temp = 0# for the temporary calculation
        count = 0# for number of even digits number
        for x in nums:
            temp = len(str(x))
            if temp%2 == 0:
                count+=1
        return count