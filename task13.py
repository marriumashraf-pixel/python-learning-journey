num = []
for i in range(5):
    num.append(int(input("Enter a number: ")))
for i in range(5):
    print(num)
    print("The maximum number is:", max(num))
    print("The minimum number is:", min(num))
    print("The sum of all numbers is:", sum(num))
    print("The average of all numbers is:", sum(num) / len(num))
for i in range(5):
    print((num[i]), "is even" if num[i] % 2 == 0 else "is odd")
