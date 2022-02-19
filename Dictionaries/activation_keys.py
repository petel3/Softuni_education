activation_keys_raw=input()
commands=input()
while commands !="Generate":
    data=commands.split(">>>")
    if data[0]== "Contains":
        substring=data[1]
        if substring not in activation_keys_raw:
            print("Substring not found!")
        else:
            print(f"{activation_keys_raw} contains {substring}")
    elif data[0]== "Flip":
        start_index=int(data[2])
        end_index=int(data[3])
        first_part=activation_keys_raw[:start_index]
        to_change=activation_keys_raw[start_index:end_index]
        end_part=activation_keys_raw[end_index:]
        if data[1] == "Upper":
            to_change=to_change.upper()
            activation_keys_raw=first_part+to_change+end_part
            print(activation_keys_raw)
        elif data[1] == "Lower":
            to_change=to_change.lower()
            activation_keys_raw = first_part + to_change + end_part
            print(activation_keys_raw)
    elif data[0]== "Slice":
        start_index=int(data[1])
        end_index=int(data[2])
        first_part = activation_keys_raw[:start_index]
        end_part = activation_keys_raw[end_index:]
        activation_keys_raw=first_part+end_part
        print(activation_keys_raw)
    commands=input()
print(f"Your activation key is: {activation_keys_raw}")