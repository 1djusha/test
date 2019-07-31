# python 3
# bulleted list

import sys, pyperclip

text = pyperclip.paste()

# TODO: split string and add *
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

print(lines)
text = '\n'.join(lines)

print(text)
pyperclip.copy(text)
