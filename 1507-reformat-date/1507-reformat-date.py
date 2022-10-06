class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        
        year = date[-4:]
        day, month = '', ''
        
        for char in date[:4]:
            if char.isnumeric():
                day += char
            else:
                break
        
        if int(day) < 10:
            day = '0' + day # convert to 2-digit format if needed0
            
        for char in date[4:]:
            if char == ' ':
                continue
            elif char.isalpha():
                month += char
            else:
                break
        
        new_month = months[month]
        
        return year + '-' + new_month + '-' + day