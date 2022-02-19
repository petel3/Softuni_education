import re
total_calories=0
counter=0
validator={}
pattern= r'(?P<sep>[|]|#)(?P<Product>[A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+)(?P=sep)' \
         r'(?P<Exp_date>[\d]{2}\/[\d]{2}\/[\d]{2})(?P=sep)(?P<Calories>[\d]+)(?P=sep)'
word=input()
validate=re.finditer(pattern,word)
for match in validate:
    if 0<int(match.group("Calories"))<10000:
        total_calories+=int(match.group("Calories"))
counter+=total_calories//2000
print(f"You have food to last you for: {counter} days!")
for valid in re.finditer(pattern,word):
    validator=valid.groupdict()
    print(f"Item: {validator['Product']}, Best before: {validator['Exp_date']}, Nutrition: {validator['Calories']}")



