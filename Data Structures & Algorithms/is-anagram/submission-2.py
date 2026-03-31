class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}

        for i in s:
            if i in sd:
                sd[i] += 1
            else:
                sd[i] = 1
        
        st = {}

        for i in t:
            if i in st:
                st[i] += 1
            else:
                st[i] = 1
        
        return sd == st