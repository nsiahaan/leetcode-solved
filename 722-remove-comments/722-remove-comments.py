class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        final = []
        current = ""
        
        for i in range(len(source)):
            line = source[i]
            j = 0
            while j < len(line):
                if line[j] == '/':
                    if j+1 < len(line):
                        if line[j+1] == '/' and not in_block: # line comment
                            break
                        elif line[j+1] == '*' and not in_block:
                            in_block = True
                            j += 1
                        elif not in_block:
                            current += line[j]
                    elif not in_block:
                        current += line[j]
                elif line[j] == '*':
                    if j+1 < len(line):
                        if line[j+1] == '/' and in_block:
                            in_block = False
                            j += 1
                        elif not in_block:
                            current += line[j]
                    elif not in_block:
                        current += line[j]
                else:
                    if not in_block:
                        current += line[j]
                j += 1
            if len(current) > 0 and not in_block:
                final.append(current)
                current = ""
                
        return final