class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        cur_len = ""
        print(s)
        i = 0
        while i < len(s):
            if s[i] != "#":
                cur_len += s[i]
                i += 1
            else:
                res.append(s[i+1: i+int(cur_len)+1])
                i += int(cur_len) + 1
                cur_len = ""

        return res
                

