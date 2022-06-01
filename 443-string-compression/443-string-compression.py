class Solution:
    def compress(self, chars: List[str]) -> int:
        start, nxt = 0, 0
        s = ""
        
        while nxt < len(chars):
            s += chars[start] # append the char
            counter = 1
            nxt += 1 # move nxt to count consecutive repeating chars -> need counter
            while nxt < len(chars) and chars[nxt] == chars[start]:
                counter += 1
                nxt += 1
            if counter > 1:
                s += str(counter) # add counter value to s
            start = nxt # move start to nxt (next new char)
            
        chars.clear()
        for i in range(len(s)):
            chars.append(s[i])
            
        return len(chars)