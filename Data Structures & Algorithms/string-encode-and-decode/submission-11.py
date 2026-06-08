class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_list = []
        for s in strs:
            enc_list.append(str(len(s)))
            enc_list.append("#")
            enc_list.append(s)
        return "".join(enc_list)
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            w_len = int(s[i:j])
            dec.append(s[j+1:j+1+w_len])
            i = j+ w_len +1
        return dec