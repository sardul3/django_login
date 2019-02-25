import re

patterns = ['sagar', 'suvash', 'saransh']

text = 'Once upon a time, there were two boys, named sagar and suvash'

for pattern in patterns:
    print('Looking for '+ pattern)

    if(re.search(pattern, text)):
        print('Match found')
    else:
        print('No match')
