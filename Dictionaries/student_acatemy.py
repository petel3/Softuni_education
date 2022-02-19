n=int(input())
academy_dict={}
for _ in range(n):
    students=input()
    grade=float(input())
    if students not in academy_dict.keys():
        academy_dict[students]=[]
    academy_dict[students].append(grade)
for student,grades in academy_dict.items():
    average_grades=sum(grades)/len(grades)
    academy_dict[student]=average_grades
academy_dict=dict(sorted(academy_dict.items(), key=lambda kvp: -kvp[1]))
for student,grades in academy_dict.items():
    if grades>=4.50:
        print(f"{student} -> {grades:.2f}")
