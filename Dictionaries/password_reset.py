raw_password=input()
command=input()

while command !="Done":
    data=command.split()
    if data[0] == "TakeOdd":
        new_raw_password = ''
        for ch in range(1,len(raw_password),2):
            new_raw_password+=raw_password[ch]
        raw_password=new_raw_password
        print(raw_password)
    elif data[0] == "Cut":
        index=int(data[1])
        length=int(data[2])

        to_remove=raw_password[index:index+length]
        raw_password=raw_password.replace(to_remove,"",1)
        print(raw_password)
    elif data[0] == "Substitute":
        substring=data[1]
        substitute=data[2]
        if substring in raw_password:
            raw_password=raw_password.replace(substring,substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")
    command=input()
print(f"Your password is: {raw_password}")