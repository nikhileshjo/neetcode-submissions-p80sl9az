class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ar = 0

        for i, h in enumerate(heights):
            curr_h = h
            j = i - 1
            k = i + 1

            while j >= 0 and heights[j] >= h and k < len(heights) and heights[k] >= h:
                curr_h += (2*h)
                j -= 1
                k += 1
            while j >= 0 and heights[j] >= h:
                curr_h += h
                j -= 1
            while k < len(heights) and heights[k] >= h:
                curr_h += h
                k += 1
            
            max_ar = max(max_ar, curr_h)
        
        return max_ar