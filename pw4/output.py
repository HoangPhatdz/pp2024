def list_students(students):
    if not students:
        print("There aren't any students")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. Name: {student.id} - {student.name} - {student.dob}")

def list_courses(courses):
    if not courses:
        print("There aren't any courses.")
    else:
        for i, course in enumerate(courses, 1):
            print(f"{i}. Name: {course.id} - {course.name}")

def list_marks(selected_course, marks):
    print(f"Student marks for course {selected_course.name}: ")
    for mark in marks:
        if mark.course_name == selected_course.name:
            print(f"Student: {mark.student_name} - Mark: {mark.mark}")
            
def list_students_by_gpa(gpa_list):
    print("List of students sorted by GPA:")
    for i, (student_name, gpa) in enumerate(gpa_list, 1):
        print(f"{i}. Student: {student_name} - GPA: {gpa:.2f}")
