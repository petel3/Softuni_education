commands=input()
students={}
while ":" in commands:
    data=commands.split(":")
    name,student_id,course=data[0],int(data[1]),data[2]
    if course not in students:
        students[course]={}
    students[course][student_id]=name
    commands=input()
searched_course=commands
searched_course_list= searched_course.split("_")
searched_course= ' '.join(searched_course_list)
for course in students:
    if course==searched_course:
        for student_id,name in students[course].items():
            print(f"{name} - {student_id}")