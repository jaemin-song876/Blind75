class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        width = len(height)
        left = 0
        right = len(height) -1

        while left<right:#두 포인터가 만날때까지
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_area


        
        