print("Welcome to the Student Management System")
print("1. Add Student \n 2. Display Students \n 3. Calculate Average Marks \n 4. Search Student by Name \n 5. Exit")
students=[]
def add_student():
    student_count = int(input("Enter the number of students: "))
    for i in range(student_count):  
        student = {
            
            "name": input("Enter student name: "),
            "age": int(input("Enter student age: ")),
            "grade": input("Enter student grade: "),
        "marks": float(input("Enter student marks: "))
    }
        students.append(student)
def display_students(students):
    print("Student List:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}")
def calculate_average_marks(students):
    total_marks = sum(student['marks'] for student in students)
    average_marks = total_marks / len(students)
    return average_marks
def search_student_by_name(students, name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return False
def main():
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            print("Average Marks:", calculate_average_marks(students))
        elif choice == '4':
            name = input("Enter the student name to search: ")
            student = search_student_by_name(students, name)
            if student:
                print(f"Found Student - Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}")
            else:
                print("Student not found.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main() 