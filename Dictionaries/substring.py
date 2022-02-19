substring=input()
word=input()

while substring in word:
    word=word.replace(substring,"")
print(word)