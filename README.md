This program is a simple weekly expense tracker that helps a student monitor their spending based on a set budget. It first defines different expense categories such as food, transportation, mobile/internet, school supplies, and entertainment, then asks the user to input their name and weekly budget with input validation to ensure only numbers are accepted. After displaying the categories, the program allows the user to enter up to four expenses by selecting a category, providing a description, and entering the amount spent, while also checking for invalid inputs and flagging any expense that exceeds 25% of the budget as a high expense. All valid expenses are stored in a list, then the program calculates the total amount spent, determines the remaining budget, and checks whether the user is within or over budget. Finally, it displays a formatted report showing all expenses, total spending, remaining balance, and a status message indicating if the budget was managed well or exceeded.

# List of expense categories with examples
categories = [
    ("Food & Drinks", "Lunch, snacks, coffee"),
    ("Transportation", "Bus, jeepney, ride-share"),
    ("Mobile / Internet", "Load, data plan, WiFi top-up"),
    ("School Supplies", "Notebook, pen, bond paper"),
    ("Entertainment", "Games, movies, hangout")
]

# Ask for student name
name = input("Student name: ")

# Input validation for weekly budget (must be a number)
while True:
    try:
        budget = float(input("Weekly budget: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display header for categories
print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

# Display all categories with numbering and examples
for i in range(len(categories)):
    print(str(i+1) + ". " + categories[i][0] + " [e.g. " + categories[i][1] + "]")

print("==========================================")

# List to store all expenses
expenses = []

# Loop to allow up to 4 expense entries
for i in range(4):
    print("\n--- EXPENSE " + str(i+1) + " ---")

    # Input validation for category selection
    while True:
        try:
            cat_num = int(input("Category (0 to skip): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Skip if user enters 0
    if cat_num == 0:
        continue

    # Check if category is valid
    if cat_num >= 1 and cat_num <= 5:
        # Get expense description
        desc = input("Description: ")

        # Input validation for amount
        while True:
            try:
                amount = float(input("Amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Flag if expense is more than 25% of budget
        flag = ""
        if amount > 0.25 * budget:
            flag = "! High Expense Alert!"

        # Store expense in list
        expenses.append([categories[cat_num - 1][0], desc, amount, flag])
    else:
        print("Invalid category. Skipped.")

# Calculate total expenses
total = 0
for i in range(len(expenses)):
    total = total + expenses[i][2]

# Calculate remaining budget
remaining = budget - total

# Check budget status
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# Display final report header
print("\n======================================================")
print("     " + name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

# Display budget
print("  Weekly Budget  : P" + str(budget))

# Display all recorded expenses
num = 1
for i in range(len(expenses)):
    print("  [" + str(num) + "] " + expenses[i][0])
    print("      " + expenses[i][1] + "   P" + str(expenses[i][2]) + "  " + expenses[i][3])
    num = num + 1

# Display summary
print("------------------------------------------------------")
print("  Total Spent    : P" + str(total))
print("  Remaining      : P" + str(remaining))
print("  Status         : " + status)
print("======================================================")
