# importing the library
from memory_profiler import profile

class Solution(object):
    # instantiating the decorator
    @profile
    def sum(self, num1: int, num2: int) -> int:
        if  -100 <= num1 and num1 <= 100 and -100 <= num2 and num2 <= 100:
            print("Sum of two numbers is: ", num1+num2)
            return num1+num2

if __name__ == '__main__':
    s = Solution()
    s.sum(10, 20)
    