word=input()
digits=""
letters=""
others=""
for ch in word:
    if ch.isalpha():
        letters+=ch
    elif ch.isdigit():
        digits+=ch
    else:
        others+=ch
print(digits)
print(letters)
print(others)