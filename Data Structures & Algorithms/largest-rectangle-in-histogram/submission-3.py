class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair : (index, height)

        for i, h in enumerate(heights):
            start = i
            # If top of stack is greater than current h, pop it.
            # Calculate the height it can make up till current h
            # Because up till then, it's not popped(meaning nothing's been shorter than it up till now)
            # so (i - index) is valid area.
            # But, what about the area it could've made backwards?
            # That's calculated by the while loop, if the previous to it was equal or lesser
            # than it, but it's greater than the current h, that area will be calculated in the next
            # iteration of the while loop.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index # it marks till where can curr h calculate valid height backwards
            stack.append((start, h))

            # this for loop will calculate all the areas towards to forward
            # till the end of the list
            # We can safely calculate all the way till the end index
            # Because the above loop gurentees that we are left with a list of
            # non - decreasing heights
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea    
        