class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []

        for i in range(len(temperatures)):
            
            while temp_stack and temp_stack[-1][0] < temperatures[i]:
                p_temp = temp_stack.pop()
                res[p_temp[1]] = i - p_temp[1]
            
            temp_stack.append([temperatures[i], i])
        
        return res