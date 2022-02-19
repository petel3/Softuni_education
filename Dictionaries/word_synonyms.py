n=int(input())
synonyms={}
for _ in range(n):
    words=input()
    synonym=input()
    if words not in synonyms.keys():
        synonyms[words]= []

    synonyms[words].append(synonym)
for key,value in synonyms.items():
    print(f'{key} - {", ".join(value)}')