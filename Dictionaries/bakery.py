list_with_products=input().split()
products={}
for i in range(0,len(list_with_products),2):
    key=list_with_products[i]
    value=int(list_with_products[i+1])
    products[key]=value
print(products)

