# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for 
# the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution(object):
    def fizzBuzz(self, n):
        res = [None] * n
        for i in range(1, n + 1):
            mod3 = i % 3 == 0
            mod5 = i % 5 == 0
            if mod3 and mod5:
                res[i - 1] = "FizzBuzz"
            elif mod3:
                res[i - 1] = "Fizz"
            elif mod5:
                res[i - 1] = "Buzz"
            else:
                res[i - 1] = str(i)
        return res