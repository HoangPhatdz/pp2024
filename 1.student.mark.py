def get_Numbers_Of_Student():
    num_students = int(input("Insert the number of student: "))
    return num_students

def get_Number_Of_Courses():
    num_courses = int(input("Insert number of courses: "))
    return num_courses

def get_Information_Of_Student(num_students):

    list_students = []

    if (num_students == 0):
        print("There are 0 student.")
    else:
        for i in range (num_students):
            student = {}
            student['id'] = input("Student Id: ")
            student['name'] = input("Student Name: ")
            student['bod'] = input("Student DoB: ")
            print("===========================")

            list_students.append(student)
            #add info 1 student to the list
    return list_students

def get_Course_Information(num_courses):

    list_courses = []

    if (num_courses == 0):
        print("There are 0 courses.")
    else:
        for i in range(num_courses):
            course = {}
            course['id'] = input("Course ID: ")
            course['name'] = input("Course name: ")
            print("===========================")

            list_courses.append(course)
            #add info 1 course to the list
    return list_courses

def list_Student(students):
    if (len(students)==0):
        print("There aren't any students")
    else:
       for i, student in enumerate(students, 1):
           print(f"{i}. Name: {student['id']} - {student['name']} - {student['bod']}")

def list_Course(courses):
    if (len(courses)==0):
        print("There aren't any courses.")
    else:
       for i, course in enumerate(courses, 1):
           print(f"{i}. Name: {course['id']} - {course['name']}")

def input_Mark(courses, students,marks):
    picked_course = int(input("Choose the course to edit mark:"))
    selected_course = courses[picked_course]
    
    print(f"Input marks in course {selected_course['name']}:")
    for student in students:
        mark = int(input("Input mark:"))
        marks.append({'course_name':selected_course['name'], 'student_name':student['name'], 'mark':mark})
    return marks

def list_Mark(marks, courses):
    picked_course = int(input("Choose the course to view marks:"))
    selected_course = courses[picked_course]

    print(f"Student marks for course {selected_course['name']}: ")

    for mark in marks:
        if mark['course_name'] == selected_course['name']:
            print(f"Student: {mark['student_name']} - Mark: {mark['mark']}")

def main():
    courses = []
    students = []
    marks = []
    num_students = 0
    num_courses = 0
    
    while(True):
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
        print("0. Exit")

        option = int(input("Insert your choice:"))

        if (option == 0):
            break
        elif option == 1:
            num_students = get_Numbers_Of_Student() 
        elif option == 2:
            students = get_Information_Of_Student(num_students)
        elif option == 3:
            num_courses = get_Number_Of_Courses()
        elif option == 4:
            courses = get_Course_Information(num_courses)
        elif option == 5:
            list_Student(students)
        elif option == 6:
            list_Course(courses)
        elif option == 7:
            list_Course(courses)
            input_Mark(courses, students, marks)
        elif option == 8:
            list_Mark(marks, courses)


# Call the main function
if __name__ == "__main__":
    main()