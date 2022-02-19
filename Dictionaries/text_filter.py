filters=input().split(", ")
sentence=input()
for filter in filters:
    while filter in sentence:
        sentence=sentence.replace(filter,len(filter)*"*")
print(sentence)