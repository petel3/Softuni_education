product_list=input().split()
needed_products=input().split()
dict_products={}
for i in range(0,len(product_list),2):
    products=product_list[i]
    quantity=int(product_list[i+1])
    dict_products[products]=quantity
for product in needed_products:
    if product in dict_products.keys():
        print(f"We have {dict_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")