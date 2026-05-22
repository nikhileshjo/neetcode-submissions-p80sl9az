class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result = result + str(len(s)) + "^" + s
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        output = []

        i = 0

        while i < len(s):
            num_str = ""
            while s[i] != '^':
                num_str += s[i]
                i += 1
            in_len = int(num_str)
            output.append(s[i+1: i+in_len+1])
            i = i + in_len + 1
        return output