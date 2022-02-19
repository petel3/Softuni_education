command=input()
users={}
while command !="End":
    data=command.split(" -> ")
    for items in range(0,len(data),2):
        company=data[items]
        id_user=data[items+1]

        if company not in users:
            users[company]=[]
        if id_user not in users[company]:
            users[company].append(id_user)

    command=input()
for company_name,username in sorted(users.items(),key=lambda kvp: kvp[0]):
    print(f"{company_name}")
    for id_users in username:
        print(f"-- {id_users}")