class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1]*n

        #pass 1: left to right
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]

        right = 1
        #pass 2: right to left
        for i in range(n-1,-1,-1):
            answer[i] *= right
            right = nums[i]*right

        return answer
