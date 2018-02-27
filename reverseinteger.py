class Solution:
    def reverse(self, x):        
        if x > 0:
            if x >= (1<<31):
                return 0
            else:
                return int(str(x)[::-1])
        else:
            a = abs(x)
            if a >= (1<<31):
                return 0
            else:
                num = int(str(a)[::-1])
                negnum = -1 * num 
                return negnum

    reverse(0, 123)