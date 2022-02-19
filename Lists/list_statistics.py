n=int(input())
positives_counter=0
positives=[]
negatives=[]
negatives_sum=0
for num in range(n):
    current_num=int(input())
    if current_num>0:
        positives_counter+=1
        positives.append(current_num)
    else:
        negatives_sum+=current_num
        negatives.append(current_num)
print(positives)
print(negatives)
print(f"Count of positives: {positives_counter}. Sum of negatives: {negatives_sum}")
