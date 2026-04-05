class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ar = 0

        for i, h in enumerate(heights):
            curr_h = h
            l = len(heights)
            j = i - 1
            k = i + 1

            while j >= 0 and heights[j] >= h and k < len(heights) and heights[k] >= h:
                j -= 1
                k += 1
            while j >= 0 and heights[j] >= h:
                j -= 1
            while k < len(heights) and heights[k] >= h:
                k += 1
            
            max_ar = max(max_ar, h * (k-j-1))
        
        return max_ar