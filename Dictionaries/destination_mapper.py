import re


pattern= r"(\=|\/)(?P<city>[A-Z][A-Za-z]{2,})\1"
destinations=input()
matches=re.finditer(pattern,destinations)
counter=0
going_to=[]
for i in matches:
    going_to.append(i.group("city"))
    counter+=len(i.group("city"))
print((f"Destinations: {', '.join(going_to)}\nTravel Points: {counter}"))
