import re
pattern= r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
numbers=input()
matches=re.finditer(pattern,numbers)
valid_nums=[match.group() for match in matches]
print(*valid_nums)