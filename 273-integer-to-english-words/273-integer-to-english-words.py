import math
class Solution:
    def threeDigits(self, num: int) -> str:
        numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        
        final = ''
        strnum = str(num)
        
        if len(strnum) == 3 and strnum[0] != '0': # hundreds
            final += numbers[int(strnum[0])] + ' Hundred '
        
        if len(strnum) >= 2:
            if strnum[-2] == '1':
                final += teens[int(strnum[-1])]
                return final
            elif strnum[-2] != '0': # tens
                final += tens[int(strnum[-2])]
                if strnum[-1] != '0':
                    final += ' '
        
        if strnum[-1] != '0':
            final += numbers[int(strnum[-1])]
        
        return final.strip()
    
    def numberToWords(self, num: int) -> str:
        suffix = ['', 'Thousand', 'Million', 'Billion']
        final = ''
        
        if num == 0:
            return 'Zero'
        
        # parse into groups of 3, then add appropriate suffix
        for i in range(len(suffix)):
            if num % 1000 != 0:
                final = self.threeDigits(num%1000) + ' ' + suffix[i] + ' ' + final           
            num = int(num / 1000)
        
        return final.strip() # remove ending spaces