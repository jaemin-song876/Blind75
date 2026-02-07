class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #sort하면 오래걸리니까 덧셈으로 찾기
        n = len(nums)
        total_sum = sum(range(n+1))

        actual_sum = sum(nums)

        return total_sum - actual_sum