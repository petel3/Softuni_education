factor=int(input())
counter=int(input())
number_for_list=1
my_list=[]
for n in range(1,counter+1):
    number_for_list=n*factor
    my_list.append(number_for_list)
print(my_list)