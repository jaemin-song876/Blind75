class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for a in range(0, n-2):
            
            #a가 직전숫자랑 똑같으면 스킵
            if a>0 and nums[a] == nums[a-1]:
                continue

            b = a+1
            c = n-1

            while b<c:
                current_sum = nums[a] + nums[b] + nums[c]

                if current_sum == 0:
                    res.append([nums[a], nums[b], nums[c]])

                    while b<c and nums[b] == nums[b+1]:
                        b += 1
                    while b<c and nums[c] == nums[c-1]:
                        c -= 1

                    b +=1
                    c -=1

                #case2: sum이 0보다 작을때
                elif current_sum <0:
                    b +=1

                #case3: sum이 0보다 클때
                else:
                    c-=1
        return res



                                                               