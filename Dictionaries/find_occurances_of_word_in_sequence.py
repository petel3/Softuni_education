import re
text=input()
word=input()
pattern = rf'\b{word}\b'
matches=len(re.findall(pattern,text, flags=re.IGNORECASE))

print(matches)