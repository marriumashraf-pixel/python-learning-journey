Students =[
    {"name": "mimi", "marks": [85, 90, 78], "age": 21},
    {"name": "ali", "marks": [92, 88, 95], "age": 23}
]
def diplay_students(students):
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}, Age: {student['age']}")
def calculate_average_marks(students):
    for student in students:
        average_marks = sum(student['marks']) / len(student['marks'])
        print(f"Average marks of {student['name']}: {average_marks}")
calculate_average_marks(Students)
name = input("Enter name of student to search: ")
for student in Students:
    if student['name'] == name:
        print(f"Name: {student['name']}, Marks: {student['marks']}, Age: {student['age']}")
else:
    print("Student not found.")