class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        aux = []
        for i in nums:
            if i not in aux:
                aux.append(i)
        print("Nums =", nums)
        print("Aux = ", aux)
        
        nums.clear()
        
        print("Nums_empt = ",nums)
        
        for j in aux:
            nums.append(j)
        
        print("New nums = ", nums)
        
        k = len(aux)
        return k
        