class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        n = len(target)
        shortest = 0
        operations = 0

        for i in range(n):
            if i + 1 < n and target[i] > target[i + 1]:
                operations += target[i] - shortest
                shortest = target[i + 1]
                
        return operations