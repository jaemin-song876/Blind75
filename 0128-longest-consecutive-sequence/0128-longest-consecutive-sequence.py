class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1. make set
        num_set = set(nums)
        longest_streak = 0

        #2. find starting point
        for n in num_set:
            if (n-1) not in num_set:
                current_num = n
                current_streak = 0

                #3. count
                while current_num in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
