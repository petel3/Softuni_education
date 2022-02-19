import re
pattern_for_print=[]
text=input()
list_of_emojis=[]
emoji = r'(?P<scope>\:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=scope)'
digits= r'\d'
cool_threshold=1
emoji_coolness=0
emoji_count=0
match_digits= re.findall(digits,text)
for digit in match_digits:
    digit=int(digit)
    cool_threshold *=digit
print(f"Cool threshold: {cool_threshold}")
for match in re.finditer(emoji,text):
    data=match.groupdict()
    emoji_count+=1
    emoji=data['emoji']
    emoji_coolness=sum([ord(letter) for letter in emoji])
    if emoji_coolness>=cool_threshold:
        result=f"{data['scope']}{emoji}{data['scope']}"
        pattern_for_print.append(result)
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in pattern_for_print:
    print(emoji)