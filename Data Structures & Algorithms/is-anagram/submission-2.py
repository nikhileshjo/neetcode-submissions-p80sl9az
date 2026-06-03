class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting
        return sorted(s) == sorted(t)