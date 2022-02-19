countries=input().split(", ")
capitals=input().split(", ")

capitals_dict=dict(zip(countries, capitals))
for key,value in capitals_dict.items():
    print(f"{key} -> {value}")
