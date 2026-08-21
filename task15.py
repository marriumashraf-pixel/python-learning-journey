expense = []
num = int(input("How many expenses do you want to enter? "))
for i in range(num):
    name = input("Enter the expense name: ")
    amount = float(input("Enter the amount: "))
    expense.append((name, amount))
def calculate_total(expense):
    total = sum(amount for _, amount in expense)
    return total
print(calculate_total(expense))