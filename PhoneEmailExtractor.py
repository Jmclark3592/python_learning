import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #match either 3 digits or an open parenthesis followed by 3 digits ending with parenthesis. 
    (\s|-|\.)? #match either a whitespace character, dash or period, or optionally (?) none of them
    (\d{3}) #match any three digits
    (\s|-|\.) #match either a whitespace character, dash or period
    (\d{4}) #match any three digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #optionally, match zero or any whitespace, ext, or x, or ext., followed by any amount or no whitespace, and 2to 5 digits
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #match 1 or more (+) of any of the ranges (-) or those characters listed in square brackets []
    @
    [a-zA-Z0-9.-]+ #match 1 or more (+) of any of the ranges (-) or those characters listed in square brackets []
    (\.[a-zA-Z]{2,4}) #match a period and any letter ranges in brackets [] 2 to 4 times (2-4 letters)
    )''', re.VERBOSE)

text = str(pyperclip.paste()) #text on clipboard is assigned to variable text
matches = []
for groups in phoneRegex.findall(text): #Searches text in clipboard that matches phoneRegex
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #join groups 1, 3, 5 and possibly 8 (below)
    if groups[8] != '': #if not an empty string...
        phoneNum += ' x' + groups[8] #then add x and group 8 (the extension)
    matches.append(phoneNum) #adds phone number to matches list

for groups in emailRegex.findall(text): #Searches text in clipboard that matches emailRegex
    matches.append(groups[0]) #for each group found this adds to matches list. Only one group in emailRegex so [0] applies.

#In Python's re module, each pair of parentheses in a regular expression creates a "group"

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard: ")
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')