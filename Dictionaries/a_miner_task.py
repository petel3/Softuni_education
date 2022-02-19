command=input()
miner_dict={}
while not command=="stop":
    value=int(input())
    if command not in miner_dict:
        miner_dict[command]=value
    else:
        miner_dict[command] += value
    command=input()
for key,value in miner_dict.items():
    print(f"{key} -> {value}")