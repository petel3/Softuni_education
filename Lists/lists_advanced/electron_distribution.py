electrons_input=int(input())
distribution=[]
num=1
while not electrons_input<=0:
    chemistry_formula=2*num**2
    if chemistry_formula<=electrons_input:
        distribution.append(chemistry_formula)
        num+=1
    else:
        distribution.append(electrons_input)
        electrons_input=0
    electrons_input -= chemistry_formula
print(distribution)