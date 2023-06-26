#EmailChecker

import pyperclip, re

webRegex = re.compile(r'''(
    (Http://|http://|https://|Https://|Www.|www.) #better would be (https?://)?
    ([^.]+) #redo
    (.com) #redo
    )''', re.VERBOSE)


text = str(pyperclip.paste()) #text on clipboard is assigned to variable text
matches = []
for groups in webRegex.findall(text): #Searches text in clipboard that matches emailRegex
    matches.append(groups[0]) #for each group found this adds to matches list. Only one group in emailRegex so [0] applies.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard: ")
    print('\n'.join(matches))
else:
    print('No web addresses found')

#In Python's re module, each pair of parentheses in a regular expression creates a "group"

