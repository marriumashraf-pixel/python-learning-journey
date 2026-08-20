stud = int(input("Enter number of students: "))
students = []
for i in range(stud):
    student_name = input(f"Enter name of student : ")
    student_marks = [int(input(f"Enter marks for subject :"))]
    students.append({"name": student_name, "marks": student_marks})

for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")