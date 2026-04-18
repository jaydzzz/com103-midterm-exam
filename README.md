**List of expense categories with example items**
categories = [
    ("Food & Drinks", "Lunch, snacks, coffee"),
    ("Transportation", "Bus, jeepney, ride-share"),
    ("Mobile / Internet", "Load, data plan, WiFi top-up"),
    ("School Supplies", "Notebook, pen, bond paper"),
    ("Entertainment", "Games, movies, hangout")
]

**Ask user for student name**
name = input("Student name: ")

**Ask user for weekly budget and convert it to float**
budget = float(input("Weekly budget: "))

**Display category section header**
print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

**Display all categories with numbering and examples**
for i in range(len(categories)):
    print(str(i+1) + ". " + categories[i][0] + " [e.g. " + categories[i][1] + "]")

print("==========================================")

**List to store all entered expenses**
expenses = []

**Loop for entering up to 4 expenses**
for i in range(4):
    print("\n--- EXPENSE " + str(i+1) + " ---")

  **Ask user to choose a category number (0 = skip)**
    cat_num = int(input("Category (0 to skip): "))

  **Skip this entry if user enters 0**
    if cat_num == 0:
        continue

  **Check if category number is valid**
    if cat_num >= 1 and cat_num <= 5:
  **Get description of expense**
        desc = input("Description: ")

  **Get amount spent and convert to float**
        amount = float(input("Amount: "))

  **Flag high expense if it exceeds 25% of budget**
        flag = ""
        if amount > 0.25 * budget:
            flag = "! High Expense Alert!"

  **Store expense data in list**
        expenses.append([categories[cat_num - 1][0], desc, amount, flag])
    else:
        # If invalid category is entered
        print("Invalid category. Skipped.")

**Initialize total expense counter**
total = 0

**Sum all expense amounts**
for i in range(len(expenses)):
    total = total + expenses[i][2]

**Compute remaining budget**
remaining = budget - total

**Check if user stayed within budget or overspent**
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

**Display final report header**
print("\n======================================================")
print("     " + name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

**Display weekly budget**
print("  Weekly Budget  : P" + str(budget))

**Display all recorded expenses**
num = 1
for i in range(len(expenses)):
    print("  [" + str(num) + "] " + expenses[i][0])
    print("      " + expenses[i][1] + "   P" + str(expenses[i][2]) + "  " + expenses[i][3])
    num = num + 1

**Display summary of spending**
print("------------------------------------------------------")
print("  Total Spent    : P" + str(total))
print("  Remaining      : P" + str(remaining))
print("  Status         : " + status)
print("======================================================")
