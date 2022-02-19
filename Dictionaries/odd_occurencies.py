words=input().split()
dictionary={}
for word in words:
    words_lower=word.lower()
    if words_lower not in dictionary:
        dictionary[words_lower]=0
    dictionary[words_lower]+=1
for key,value in dictionary.items():
    if value%2!=0:
        print(key, end=" ")
