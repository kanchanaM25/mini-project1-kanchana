class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}"


class CollegeManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        course = input("Enter course: ")
        new_student = Student(student_id, name, course)
        self.students.append(new_student)
        print(f'Student added: {new_student}')

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("Student List:")
            for student in self.students:
                print(student)

    def delete_student(self):
        self.view_students()
        if self.students:
            student_id = input("Enter the student ID to delete: ")
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    print(f'Student removed: {student}')
                    return
            print("Student ID not found.")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    cms = CollegeManagementSystem()
    cms.run()
