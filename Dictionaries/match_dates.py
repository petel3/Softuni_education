import re
pattern = r"(?P<Day>\d{2})(?P<separators>\-?\/?\.?)(?P<Month>[A-Z][a-z]{2})(?P=separators)(?P<Year>\d{4})"
dates=input()
matches = re.finditer(pattern, dates)
for date in matches:
    current_date=date.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")