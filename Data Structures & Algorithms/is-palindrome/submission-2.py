class Solution:
    def isPalindrome(self, s: str) -> bool:
         # .isalnum()
        if s == "":
            return True

        n = len(s)
        i = 0
        j = n-1

        while i < j:
            print(i,j)
            f = s[i].lower()
            b = s[j].lower()

            if not f.isalnum():
                i+=1
                continue
            if not b.isalnum():
                j-=1
                continue
            if f != b:
                print(f,b, f==b)
                return False
            i+=1
            j-=1
        
        return True
