list_of_strings=input().split()
list_of_integers=[]
reversed_integers=[]
for index in list_of_strings:
    list_of_integers.append(int(index))
for el in list_of_integers:
    reversed_integers.append(el*(-1))
print(reversed_integers)
