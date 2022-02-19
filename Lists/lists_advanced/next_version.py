last_version=input().split(".")
next_version_list=[]
next_version="".join(last_version)
next_version=int(next_version) +1
next_version=str(next_version)
for n in next_version:
    next_version_list.append(n)
print(".".join(next_version_list))