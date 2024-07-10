# importing the library
from memory_profiler import profile
import unittest 

class Solution(object):
    # instantiating the decorator
    @profile
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = [] 
        for i in accounts:
            wealth.append(sum(i))
        return max(wealth)


if __name__ == '__main__':
    s = Solution()
    assert s.maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert s.maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17