input_list_of_numbers=[int(n) for n in input().split(", ")]
i=0
while len(input_list_of_numbers)>0:
    i+=10
    current_group=[num for num in input_list_of_numbers if num<=i]
    print(f"Group of {i}'s: {current_group}")
    for eraser in current_group:
        input_list_of_numbers.remove(eraser)
