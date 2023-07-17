#https://leetcode.com/problems/fizz-buzz/
#my submission: https://leetcode.com/submissions/detail/996299762/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
                i += 1
            elif i % 3 == 0:
                arr.append("Fizz")
                i += 1
            elif i % 5 == 0:
                arr.append("Buzz")
                i += 1
            else:
                arr.append(str(i))
                i += 1
        return arr