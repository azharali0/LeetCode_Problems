class Solution:
    def findMaxConsecutiveOnes(self, num: List[int]) -> int:
        nums = 0
        count = 0
        for x in num:
            if x==1:
                nums+=1
            if x==0:
                if nums > count:
                    count = nums
                nums = 0
        if nums > count:
            count = nums
        return count
    

                
        