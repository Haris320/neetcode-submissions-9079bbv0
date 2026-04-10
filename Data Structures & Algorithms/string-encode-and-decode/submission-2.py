class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''

        for word in strs:
            l = str(len(word))
            s += l + "#" + word
        print(s)
        return s
        
    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0

        while i < len(s):
            j = i
            # find the '#'
            while s[j] != '#':
                j += 1

            # length is from i to j
            wordLen = int(s[i:j])

            # extract the word
            arr.append(s[j+1 : j+1+wordLen])

            # move i to the start of the next token
            i = j + 1 + wordLen

        return arr
