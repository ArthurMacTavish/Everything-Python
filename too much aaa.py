import pyperclip

num = 0
tooMuchA = 'A'

while num <= 15:
    tooMuchA = tooMuchA + tooMuchA
    num = num + 1

pyperclip.copy(tooMuchA)