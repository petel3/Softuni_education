import re


regex=r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names=input()
matches = re.findall(regex, names)

print(*matches)
