import re
n=int(input())
pattern_barcode= r'(?P<left_barcode>\@[#]+)(?P<name_of_barcode>[A-Z][A-Z+[a-z0-9]{4,}[A-Z])(\@[#]+)'
pattern_digits= r'\d'
for _ in range (n):
    barcode=input()

    match_digits=re.findall(pattern_digits,barcode)
    if re.match(pattern_barcode,barcode):


        if len(match_digits) == 0:
            print("Product group: 00")
        elif len(match_digits) != 0 or not match.group():
            print(f"Product group: {''.join(match_digits)}")
    else:
        print("Invalid barcode")