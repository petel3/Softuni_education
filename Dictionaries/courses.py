command=input()
courses={}
while command !="end":
    course=command.split(":")
    for item in range (0,len(course),2):
        key=course[item]
        value=course[item+1]
        if key not in courses.keys():
            courses[key]=[]
        courses[key].append(value)
    command=input()

for name_course,students in  sorted(courses.items(), key=lambda kvp: len(kvp[1]) ,reverse=True) :
    print(f"{name_course.strip()}: {len(students)}")
    for student in sorted(students):
        print(f"--{student}")