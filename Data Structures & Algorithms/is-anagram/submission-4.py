class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count array
        if len(s) != len(t):
            return False
        char_arr = [0] * 26
        for i, j in zip(s,t):
            char_arr[ord(i) - ord('a')] += 1
            char_arr[ord(j) - ord('a')] -= 1
        for k in char_arr:
            if k != 0:
                return False
        return True