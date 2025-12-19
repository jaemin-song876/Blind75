class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #1. create hashtable(dict)
        prev_map = {} #{num : index}

        #2.check the list
        for i, n in enumerate(nums):

            #3. find needed
            needed = target - n

            if needed in prev_map:
                return [prev_map[needed], i]

            prev_map[n] =i

