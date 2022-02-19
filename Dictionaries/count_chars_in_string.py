string=input().split()
string="".join(string)
value=0
dictionary={}
for char in string:
    if char not in dictionary:
        dictionary[char]=value
    dictionary[char]+=1
for key,value in dictionary.items():
    print(f"{key} -> {value}")