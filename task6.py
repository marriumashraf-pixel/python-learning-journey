def calculate_average(marks):
 return sum(marks) / len(marks)
marks = [int(input("Enter marks: ")) for i in range(5)]
average = calculate_average(marks)
print("Average marks:", average)
