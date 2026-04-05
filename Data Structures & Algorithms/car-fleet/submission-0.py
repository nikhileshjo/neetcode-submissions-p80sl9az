class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ind = sorted(range(len(position)), key = position.__getitem__, reverse = True)

        for i in ind:
            t = (target - position[i])/ speed[i]

            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)
        
        return len(stack)