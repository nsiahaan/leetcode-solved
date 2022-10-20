class Solution:
    def myAtoi(self, s: str) -> int:
        read = ''
        is_neg, is_pos = False, False
        invalid = set()
        idx = 0
        
        while idx < len(s):
            if s[idx] in invalid:
                break
            # whitespace and symbols
            if s[idx] == ' ':
                idx += 1
                continue
            if s[idx] == '-' or s[idx] == '+':
                invalid.add(' ')
                invalid.add(s[idx])
                if s[idx] == '-':
                    is_neg = True
                else:
                    is_pos = True
                idx += 1
                continue
            # read numbers
            if s[idx].isdigit():
                invalid.add('+') # symbols + nondigits no longer valid
                invalid.add('-')
                invalid.add(' ')
                if s[idx] == '0' and len(read) == 0: # ignore leading 0s
                    idx += 1
                    continue
                else:
                    read += s[idx]
                    idx += 1
            else:
                idx += 1
                break
                
        # end while loop

        if is_neg and is_pos: # invalid signs
            return 0
        
        if len(read) == 0: # nothing read
            return 0
        
        ans = int(read)
        if is_neg:
            ans *= -1
            if ans < -2147483648: # clamping 
                return -2147483648
        if ans > 2147483647:
            return 2147483647
        
        return ans