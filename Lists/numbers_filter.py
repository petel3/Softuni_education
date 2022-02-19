n=int(input())
list_of_numbers=[]
filtered_list=[]
for num in range(n):
    numbers=int(input())
    list_of_numbers.append(numbers)
command=input()
if command=="even":
    for number in list_of_numbers:
        if number%2==0 or number==0:
            filtered_list.append(number)
elif command=="odd":
    for number in list_of_numbers:
        if number%2==1:
            filtered_list.append(number)
elif command=="positive":
    for number in list_of_numbers:
        if number>=0:
            filtered_list.append(number)
elif command=="negative":
    for number in list_of_numbers:
        if number<0:
            filtered_list.append(number)
print(filtered_list)


