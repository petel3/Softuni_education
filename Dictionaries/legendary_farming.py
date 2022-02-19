def collected_materials(key_materials_dict:dict, junk_materials_dict:dict, material:str, quantity:int):
    if material=="shards" or material=="fragments" or material=="motes":
        key_materials_dict[material]+=quantity
    else:
        if material not in junk_materials.keys():
            junk_materials[material]=quantity
        else:
            junk_materials[material]+=quantity

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials={}
items_obtained=""

while items_obtained == "":
    current_line=input().split()

    for i in range (0,len(current_line),2):
        material_quantity=int(current_line[i])
        material_name=current_line[i+1].lower()
        collected_materials(key_materials,junk_materials,material_name,material_quantity)

        if key_materials['shards']>=250:
            items_obtained="Shadowmourne"
            key_materials["shards"]-=250
            break

        elif key_materials['fragments']>=250:
            items_obtained="Valanyr"
            key_materials['fragments']-=250
            break

        elif key_materials['motes']>=250:
            items_obtained="Dragonwrath"
            key_materials['motes']-=250
            break

print(f"{items_obtained} obtained!")
for (material_name,material_quantity) in sorted(key_materials.items(),key=lambda kvp:(-kvp[1],kvp[0])):
    print(f"{material_name}: {material_quantity}")
    
for (junk_materials_name,junk_materials_quantity) in sorted(junk_materials.items(), key=lambda kvp: kvp[0]):
    print(f"{junk_materials_name}: {junk_materials_quantity}")

