categories = [
    ("Food & Drinks", "Lunch, snacks, coffee"),
    ("Transportation", "Bus, jeepney, ride-share"),
    ("Mobile / Internet", "Load, data plan, WiFi top-up"),
    ("School Supplies", "Notebook, pen, bond paper"),
    ("Entertainment", "Games, movies, hangout")
]

name = input("Student name: ")
budget = float(input("Weekly budget: "))

print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

for i in range(len(categories)):
    print(str(i+1) + ". " + categories[i][0] + " [e.g. " + categories[i][1] + "]")

print("==========================================")

expenses = []

for i in range(4):
    print("\n--- EXPENSE " + str(i+1) + " ---")
    cat_num = int(input("Category (0 to skip): "))

    if cat_num == 0:
        continue

    if cat_num >= 1 and cat_num <= 5:
        desc = input("Description: ")
        amount = float(input("Amount: "))

        flag = ""
        if amount > 0.25 * budget:
            flag = "! High Expense Alert!"

        expenses.append([categories[cat_num - 1][0], desc, amount, flag])
    else:
        print("Invalid category. Skipped.")

total = 0
for i in range(len(expenses)):
    total = total + expenses[i][2]

remaining = budget - total

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("\n======================================================")
print("     " + name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")
print("  Weekly Budget  : P" + str(budget))

num = 1
for i in range(len(expenses)):
    print("  [" + str(num) + "] " + expenses[i][0])
    print("      " + expenses[i][1] + "   P" + str(expenses[i][2]) + "  " + expenses[i][3])
    num = num + 1

print("------------------------------------------------------")
print("  Total Spent    : P" + str(total))
print("  Remaining      : P" + str(remaining))
print("  Status         : " + status)
print("======================================================")