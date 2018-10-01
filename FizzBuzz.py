#replaces all multiples of 3 by Fizz, all mutiples of 5 by Buzz
#and all multiples of 3 & 5 by FizzBuzz

class Solution:
    def fizzBuzz(self, n):
        #create a list of numbers from 1 to n+1
        num = list(range(1, n+1))
        answer = []
        for i in range(n):
            if num[i]%3 == 0 and num[i]%5 == 0:
                answer.append("FizzBuzz")
            elif num[i]%3 ==0:
                answer.append("Fizz")
            elif num[i]%5 ==0:
                answer.append("Buzz")
            else:
                answer.append(str(num[i]))
        return answer
