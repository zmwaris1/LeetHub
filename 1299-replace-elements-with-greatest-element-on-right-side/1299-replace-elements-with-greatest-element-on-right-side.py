class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = max(arr[i:])
        arr.append(-1)
        arr.pop(0)
        return arr
        