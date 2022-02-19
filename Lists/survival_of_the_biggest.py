list_strings=input().split()
remover=int(input())
for i in range(len(list_strings)):
    list_strings[i]=int(list_strings[i])

for i in range(remover):
    min_element=min(list_strings)
    list_strings.remove(min_element)

for i in range(len(list_strings)):
    list_strings[i]=str(list_strings[i])
print(', '.join(list_strings))
