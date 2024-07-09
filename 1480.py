# importing the library
from memory_profiler import profile

class Solution:
    # instantiating the decorator
    @profile
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[:i+1]))
        return(result)

if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1,1,1,1,1]))