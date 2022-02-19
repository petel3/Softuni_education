def numbers_searching(*list):

    result=[]

    missing_value=[]
    sorted(list)
    max_value = max(list)
    min_value =min(list)
    for number in range(min_value,max_value+1):
        if  number not in list:
            missing_value.append(number)
        else:
            value=list.count(number)
            if value>=2:
                result.append(number)

    missing_value.append(result)
    return missing_value
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))