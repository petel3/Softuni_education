from project.student_report_card import StudentReportCard
from unittest import TestCase,main

class Test(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Pesho", 5)
    def test_student_initialization_for_valid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_name=""
        self.assertEqual("Student Name cannot be an empty string!",str(ex.exception))
        self.student.student_name="Pesho"
        self.assertEqual("Pesho",self.student.student_name)

    def test_student_initialization_for_valid_year(self):
        with self.assertRaises(ValueError) as ex:
            self.student.school_year=0
        self.assertEqual("School Year must be between 1 and 12!",str(ex.exception))
        self.student.school_year = 1
        self.assertEqual(1, self.student.school_year)

    def test_student_initialization_raise_error_for_name_and_year(self):
        with self.assertRaises(ValueError) as ex:
            student=StudentReportCard("Pesho",13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))
        with self.assertRaises(ValueError) as exept:
            student=StudentReportCard("",2)
        self.assertEqual("Student Name cannot be an empty string!",str(exept.exception))

    def test_student_initialization_attributes(self):
        student = StudentReportCard("Pesho", 12)
        self.assertEqual("Pesho",student.student_name)
        self.assertEqual(12,student.school_year)
        self.assertEqual({},student.grades_by_subject)
        self.student.grades_by_subject={"Math":[5.00,4.50]}
        self.assertEqual({"Math":[5.00,4.50]},self.student.grades_by_subject)

    def test_add_grade_method_implementation(self):
        subject="Math"
        grade=5.30
        grade2=5.50
        self.student.add_grade(subject,grade)
        subject2="Biology"
        self.assertEqual({subject:[grade]},self.student.grades_by_subject)
        self.student.add_grade(subject, grade2)
        self.assertEqual({subject: [grade,grade2]}, self.student.grades_by_subject)
        self.student.add_grade(subject2, grade2)
        self.assertEqual({subject2: [grade2],subject: [grade,grade2]}, self.student.grades_by_subject)


    def test_average_grades_by_subject_method_is_correctly_working(self):
        self.student.grades_by_subject={"Math":[6.00,2.00,6.00,2.00],"Biology":[5.00,6.00,5.00,6.00]}
        self.assertEqual(f"{'Math'}: {4:.2f}\n"f"{'Biology'}: {5.5:.2f}",self.student.average_grade_by_subject())

    def test_average_grades_for_all_subject_method_is_correctly_working(self):
        self.student.grades_by_subject = {"Math": [6.00, 2.00, 6.00, 2.00]}
        self.assertEqual(f"Average Grade: {4 :.2f}", self.student.average_grade_for_all_subjects())
        self.student.grades_by_subject={"Math": [6.00, 2.00, 6.00, 2.00], "Biology": [5.00, 6.00, 5.00, 6.00]}
        self.assertEqual(f"Average Grade: {4.75 :.2f}", self.student.average_grade_for_all_subjects())


    def test_repr_function(self):
        self.student.grades_by_subject = {"Math": [6.00, 2.00, 6.00, 2.00], "Biology": [5.00, 6.00, 5.00, 6.00]}
        expected=f"Name: {self.student.student_name}\n" \
                 f"Year: {self.student.school_year}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_for_all_subjects()}"
        self.assertEqual(expected,repr(self.student))

if __name__=="__main__":
    main