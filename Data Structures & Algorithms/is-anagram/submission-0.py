class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1, mp2 = {}, {}

        for i in s:
            if i not in mp1:
                mp1[i] = 1
            else:
                mp1[i] += 1
        for i in t:
            if i not in mp2:
                mp2[i] = 1
            else:
                mp2[i] += 1

        return mp1 == mp2
        