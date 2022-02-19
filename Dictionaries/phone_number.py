import re
pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
phones = input()
matches = re.finditer(pattern, phones)
valid_phones= [match.group() for match in matches]
print(", ".join(valid_phones))
