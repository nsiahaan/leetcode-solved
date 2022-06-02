class Solution:
    def findNthDigit(self, n: int) -> int:
        size, step, number = 9, 1, 1
        while n > (size * step): # find the right 'bucket'
            n = n - (size * step)
            size *= 10
            step += 1
            number *= 10
        
        # access the correct digit
        num = str(number + (n-1) // step)
        digit = int(num[(n - 1) % step])
        return digit