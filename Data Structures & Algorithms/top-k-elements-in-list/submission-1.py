class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums) #number, occurence
        arr = []

        for i in range(len(nums)+1):
            arr.append([])
        
        for num, occ in hashMap.items():
            arr[occ].append(num)

        res = []

        for i in range(len(arr)-1, -1, -1):
            for n in arr[i]:
                res.append(n)
            if len(res) == k:
                return res

        return []