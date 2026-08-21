task = []
num = int(input("How many tasks do you want to enter? "))
for i in range(num):
    task.append(input("Enter a task: "))
print("Your tasks:")
for number , task in enumerate(task, start=1):
    print(f"{number}: {task}")
