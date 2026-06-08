class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        w_len = ""
        ind = 0
        while ind < len(s):
            if s[ind] == "#":
                w_len = int(w_len)
                dec.append(s[ind+1:ind+w_len+1])
                ind += w_len + 1
                w_len = ""
            else:
                w_len += s[ind]
                ind += 1
        return dec