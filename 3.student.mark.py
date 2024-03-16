import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

class Mark:
    def __init__(self, course_name, student_name, mark):
        self.course_name = course_name
        self.student_name = student_name
        self.mark = mark

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def get_num_students(self):
        return int(input("Insert the number of students: "))

    def get_num_courses(self):
        return int(input("Insert number of courses: "))

    def input_student_information(self, num_students):
        for _ in range(num_students):
            student_id = input("Student Id: ")
            name = input("Student Name: ")
            dob = input("Student DoB: ")
            self.students.append(Student(student_id, name, dob))

    def input_course_information(self, num_courses):
        for _ in range(num_courses):
            course_id = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(course_id, name))

    def list_students(self):
        if not self.students:
            print("There aren't any students")
        else:
            for i, student in enumerate(self.students, 1):
                print(f"{i}. Name: {student.id} - {student.name} - {student.dob}")

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses.")
        else:
            for i, course in enumerate(self.courses, 1):
                print(f"{i}. Name: {course.id} - {course.name}")

    def input_marks(self):
        if not self.courses:
            print("Please input courses first.")
            return
        if not self.students:
            print("Please input students first.")
            return
        for student in self.students:
            mark = float(input("Input mark:"))
            mark = round(mark, 1)
            self.marks.append(Mark(selected_course.name, student.name, mark))

        picked_course = int(input("Choose the course to edit marks:"))
        selected_course = self.courses[picked_course]

        print(f"Input marks in course {selected_course.name}:")
        for student in self.students:
            mark = int(input("Input mark:"))
            self.marks.append(Mark(selected_course.name, student.name, mark))

    def list_marks(self):
        if not self.courses:
            print("Please input courses first.")
            return
        if not self.students:
            print("Please input students first.")
            return

        picked_course = int(input("Choose the course to view marks:"))
        selected_course = self.courses[picked_course]

        print(f"Student marks for course {selected_course.name}: ")

        for mark in self.marks:
            if mark.course_name == selected_course.name:
                print(f"Student: {mark.student_name} - Mark: {mark.mark}")
                
    def calculate_gpa(self, student_name):
        total_credit = 0
        weighted_sum = 0
        for mark in self.marks:
            if mark.student_name == student_name:
                credit = 1
                total_credit += credit
                weighted_sum += mark.mark * credit
        if total_credit == 0:
            return 0
        return weighted_sum / total_credit
    
    def list_students_by_gpa(self):
        gpa_list = [(student.name, self.calculate_gpa(student.name)) for student in self.students]
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        print("List of students sorted by GPA:")
        for i, (student_name, gpa) in enumerate(gpa_list, 1):
            print(f"{i}. Student: {student_name} - GPA: {gpa:.2f}")            

    def main(self):
        while True:
            print("=====================")
            print("List of actions:")
            print("1. Input number of students")
            print("2. Input information of students")
            print("3. Input number of courses")
            print("4. Input information of courses")
            print("5. List students")
            print("6. List courses")
            print("7. Select course and input marks.")
            print("8. List the marks of the chosen courses")
            print("9. List students sorted by GPA")
            print("0. Exit")

            option = int(input("Insert your choice:"))

            if option == 0:
                break
            elif option == 1:
                num_students = self.get_num_students()
            elif option == 2:
                self.input_student_information(num_students)
            elif option == 3:
                num_courses = self.get_num_courses()
            elif option == 4:
                self.input_course_information(num_courses)
            elif option == 5:
                self.list_students()
            elif option == 6:
                self.list_courses()
            elif option == 7:
                self.input_marks()
            elif option == 8:
                self.list_marks()
            elif option == 9:
                self.list_students_by_gpa()
                
school_system = SchoolManagementSystem()
school_system.main()
