import re
pattern = r'\d+'
numbers=input()
while numbers != "":
    catched_numbers=re.findall(pattern,numbers)
    if len(catched_numbers)==0:
        numbers = input()
        continue
    else:
        print(*(catched_numbers),end=" ")
    numbers=input()