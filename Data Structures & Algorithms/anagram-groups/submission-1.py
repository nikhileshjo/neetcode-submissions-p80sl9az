class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFingerPrint(word):
            finger_print = [0] * 26
            for i in word:
                finger_print[ord(i) - ord('a')] += 1
            return ','.join(map(str, finger_print))
        
        ana_group = {}

        for s in strs:
            fp = getFingerPrint(s)
            if fp in ana_group:
                ana_group[fp].append(s)
            else:
                ana_group[fp] = [s]
        return list(ana_group.values())