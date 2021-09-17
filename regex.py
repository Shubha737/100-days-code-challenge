# Day 34
# regex
# Pattern search using Regular Expression

email = ''' CoreyMSchafer@gmail.com 
Corey.schafer@university.edu 
Corey-321-schafer@my-work.net '''

import re
pattern = re.compile(r'Corey(M|\.|-)(S|s|\d\d\d)(-?s?)chafer@\w\w(-?)\w+\.\w+')
matches = pattern.finditer(email)
for match in matches :
    print (match)