# importing the library
from memory_profiler import profile
import unittest 

class Solution(object):
    # instantiating the decorator
    @profile
    def minOperations(self, logs: list[str]) -> int:
        steps: int = 0
        if 1000 > len(logs) > 0: 
            for i in logs:
                if 1 <= len(i) <= 10:
                    if i == "../":
                            steps -= 1 if steps>0 else 0
                    elif i != "./":
                        steps += 1
        return steps
    

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
    assert s.minOperations(["d1/","d2/","../","d21/","./"]) == 2
    assert s.minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]) == 2
    