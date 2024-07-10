# importing the library
from memory_profiler import profile
import unittest 

class Solution(object):
    # instantiating the decorator
    @profile
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i%3 == 0:
                result.append("Fizz")
            elif i%5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

""" 
Better Approach 100 ms faster, 100 Kb less memory 
    def fizzBuzz(self, n: int) -> List[str]:
        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]
        
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr
"""

if __name__ == '__main__':
    s = Solution()
    assert s.fizzBuzz(3) == ["1","2","Fizz"]
    