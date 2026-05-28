class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        result = []

        for a in range(n-3):
            
            if a>0 and nums[a] == nums[a-1]:
                continue

            for b in range(a+1, n-2):
                if b> a+1 and nums[b] == nums[b-1]:
                    continue

                c = b+1
                d = n-1

                while c<d:
                    current_sum = nums[a] + nums[b] +nums[c] + nums[d]

                    #case1: sum이 target이랑 같을때
                    if current_sum == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        while c<d and nums[c] == nums[c+1]:
                            c+=1
                        while c<d and nums[d] == nums[d-1]:
                            d -=1

                            
                        c += 1
                        d -= 1
                    #case2: sum이 target보다 작을때
                    elif current_sum < target:
                        c += 1

                    #case3: sum이 target보다 클때:
                    else:
                        d -= 1

        return result
                    


        