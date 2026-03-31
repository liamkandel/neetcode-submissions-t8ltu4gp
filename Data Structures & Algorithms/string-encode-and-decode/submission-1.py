class Solution:

    def encode(self, strs: List[str]) -> str:
        # go through each word in strs
        #   go through each letter in a word
        #       get the ascii val of the letter
        #       append it to s, then a space
        #       at beginning of new word, add a newline to s to delimit words
        s = ""
        for word in strs:
            for let in word:
                s = s + str(ord(let)) + " "
            s = s +  str(ord('\n')) + " "
        return s
        
    def decode(self, s: str) -> List[str]:
        # split into a list based on spaces
        # go through each element, convert it to its letter
        # if the elemtn is ord('\n'), then you've reached end of current word

        strs = []
        cur = ""
        enc = [int(x) for x in s.split()]

        for num in enc:
            c = chr(num)
            if c == '\n':
                strs.append(cur)
                cur = ""
            else:
                cur += c
        
        return strs
