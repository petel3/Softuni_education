from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.default_course="Python"
        self.default_notes=['n1','n2']
        self.student = Student("Pesho",{self.default_course:self.default_notes})

    def test_student_initialization_with_courses(self):
        self.assertEqual("Pesho",self.student.name)
        self.assertEqual({"Python":['n1','n2']},self.student.courses)

    def test_student_initialization_without_courses(self):
        student = Student("Pesho")
        self.assertEqual("Pesho", student.name)
        self.assertEqual({}, student.courses)

    def test_student_enroll_method_should_add_notes(self):
        new_notes=['n3','n4']
        expected_notes=self.default_notes + new_notes
        result=self.student.enroll(self.default_course,new_notes)

        expect = "Course already added. Notes have been updated."
        self.assertEqual(expect, result)
        self.assertTrue(self.default_course in self.student.courses)
        self.assertEqual(expected_notes,self.student.courses[self.default_course])

    def test_student_enroll_should_add_course_and_notes(self):
        expect = "Course and course notes have been added."
        for idx,command in enumerate(['','Y']) :
            course_name=f"Java{idx}"
            course_notes=["SOLID", "Inheritance"]
            result = self.student.enroll(f"{course_name}", course_notes,command)
            self.assertEqual(expect, result)
            self.assertTrue(course_name in self.student.courses)
            self.assertEqual(course_notes,self.student.courses[course_name])

    def test_student_enroll_should_add_course_without_notes(self):
        expect="Course has been added."
        course_name = f"Java"
        course_notes = ["SOLID", "Inheritance"]
        result = self.student.enroll(course_name, course_notes, "N")
        self.assertEqual(expect, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([],self.student.courses[course_name])





    def test_student_add_notes_method_is_raises_exeption(self):
        course_name = f"Java"

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name,["OOP","Advanced"])
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_student_add_notes_method_is_add(self):
        notes=f"random"
        expected_notes=[x for x in self.default_notes]
        expected_notes.append(notes)
        result=self.student.add_notes(self.default_course,notes)
        self.assertEqual("Notes have been updated",result)
        self.assertEqual(expected_notes,self.student.courses[self.default_course])

    def test_student_leave_course_method_is_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))

    def test_student_leave_course_method_is_removing_course(self):
        self.student.enroll("Java",[])
        expected_courses_count=len(self.student.courses)-1
        result=self.student.leave_course(self.default_course)
        self.assertEqual("Course has been removed",result)
        self.assertTrue(self.default_course not in self.student.courses)
        self.assertEqual(expected_courses_count,len(self.student.courses))

if __name__ == "__main__":
    main
