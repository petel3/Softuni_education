# new_list=[]
# name_list=[]
#
# n=int(input())
# dict_names={}
# for _ in range(n):
#     new_list.append([input(),float(input())])
#
# for el in new_list:
#     name,score=el
#     if score  not in dict_names:
#         dict_names[score]=[]
#     dict_names[score].append(name)
# dict_names=sorted(dict_names.items())
# dict_names.remove(dict_names[0])
# print("\n".join(sorted(dict_names[0][1])))
#


new_word=[]
chars=[]
sentence=[x for x in input()]

for ch in range (len(sentence)):

    if sentence[ch].islower():

        chars.append(sentence[ch].upper())
        continue


    if sentence[ch].isupper():
        chars.append(sentence[ch].lower())
        continue
    if sentence[ch]==" ":
        chars.append(sentence[ch])

chars =(''.join(([el for el in chars])))
for char in chars:
    new_word.append(char)

interesting=chars.split()
print(f"{' '.join(interesting[::-1])}")

