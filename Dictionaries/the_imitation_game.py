word=input()
command=input()
while command!="Decode":
    data=command.split("|")
    if data[0]=="Move":
        lenght=int(data[1])
        to_move=word[:lenght]
        left_side=word[lenght:]
        word=left_side + to_move

    elif data[0]=="Insert":
        index=int(data[1])
        value=data[2]
        word=word[:index] + value + word[index:]

    elif data[0]=="ChangeAll":
        substring=data[1]
        replacement=data[2]
        if substring in word:
            word=word.replace(substring,replacement)
    command=input()
print(f"The decrypted message is: {word}")