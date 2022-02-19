class Programmer:
    def __init__(self,name,language,skills):
        self.name = name
        self.language = language
        self.skills = skills
    def watch_course(self,course_name,language,skills_earned):
        if self.language !=language:
            return f"{self.name} does not know {language}"
        self.skills+=skills_earned
        self.language=language
        return f"{self.name} watched {course_name}"
    def change_language(self,new_language,skills_need):
        if self.skills>skills_need and self.language==new_language:
            return f"{self.name} already knows {new_language}"
        elif self.skills<skills_need:
            return f"{self.name} needs {skills_need-self.skills} more skills"
        elif self.language!=new_language:
            self.skills-=skills_need
            previous_language=self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
# #
# programmer = Programmer("Lemmy", "Java", 100)
# print(programmer.change_language("Python", 50))
#         # self.assertEqual(res, "Lemmy switched from Java to Python")
#         # self.assertEqual(programmer.language, "Python")