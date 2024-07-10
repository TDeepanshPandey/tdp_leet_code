# importing the library
from memory_profiler import profile
import unittest 

class Solution(object):
    # instantiating the decorator
    @profile
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num /= 2 
            else:
                num -= 1
        return count

""" 
Better Approach 50 ms faster, 100 Kb less memory 
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
"""

if __name__ == '__main__':
    s = Solution()
    assert s.numberOfSteps(14) == 6
    