# Day 35 code 2
# regex_match

urls = ''' https://www.google.com
https://coreyms.com
https://www.youtube.com
https://www.nasa.gov/ '''

import re

Pattern = re.compile(r'(https)://[a-z]+\.[a-z]*(\.*)(com|gov*)')
matches = Pattern.finditer(urls)

for match in matches :
    print(match)