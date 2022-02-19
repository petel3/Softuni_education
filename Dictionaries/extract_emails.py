import re
emails = input()
pattern = r"\b[A-Za-z0-9.,_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_validator = re.findall(pattern, emails)
print('\n'.join(email_validator))