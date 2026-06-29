class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0

        while n>0:
            last_bit = n&1
            if last_bit ==1:
                count +=1

            n=n//2

        return count
