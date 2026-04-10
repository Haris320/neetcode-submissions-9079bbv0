class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} #sorted, [words]

        for i, word in enumerate(strs):
            sortW = ''.join(sorted(word))

            if sortW not in hashMap:
                hashMap[sortW] = []

            hashMap[sortW].append(word)

        res = []
        for (k,v) in hashMap.items():
            temp = []
            for word in v:
                temp.append(word)

            res.append(temp)
        
        return res

