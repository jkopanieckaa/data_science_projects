# import numpy as np
#
# n=[1,2,7]
# for a in n:
#     a *= 2
#
# print(a)
#
# numbers = [1,2,7]
# doubled = [n*2 for n in numbers]
# print(doubled)

budget = 1500
expenses = [45, 20, 80]
categories = ['food','transport','books']

total_expenses = sum(expenses)


def show_expenses(categories_student,expenses_student ):
    for x in range(len(categories_student)):
        print(categories_student[x],"-", expenses_student[x],"zł")


def calculate_remaining_budget(budget_student, expenses_student):
    sum_expenses = sum(expenses_student)
    remaining_budget = budget_student - sum_expenses
    if remaining_budget > 0:
        print(f"Budget is within normal limits: {remaining_budget}\n")
    elif remaining_budget == 0:
        print(f"Budget has been used up: {remaining_budget}\n")
    else:
        print(f"Budget has been exceeded: {remaining_budget}\n")

# big_expenses = [number for number in expenses if number > 40 ]
# # print(big_expenses)
#
# medium_expenses = [number for number in expenses if 20 < number < 80]
# # print(medium_expenses)

import numpy as np

expenses_array = np.array([45, 20, 80])
new_expenses = expenses_array * 1.20  #20% up


mask = expenses_array > 30
filtered_expenses = expenses_array[mask]

def analyze_expenses(expenses_student):
    expenses_student_array = np.array(expenses_student)
    expenses_mean = np.mean(expenses_student_array)
    mask_expenses = expenses_student_array > expenses_mean
    filtered_expenses_student = expenses_student_array[mask_expenses]
    return filtered_expenses_student



while True:
    print("\n===== STUDENT BUDGET TRACKER =====\n")
    print("1. Show all expenses")
    print("2. Check remaining budget")
    print("3. Show expenses above average")
    print("4. Exit\n")

    choice = input("Choose an option:")

    if choice == "1":
        print("")
        show_expenses(categories, expenses)
    elif choice == "2":
        print("")
        calculate_remaining_budget(budget, expenses)
    elif choice == "3":
        print("")
        print(analyze_expenses(expenses))
    elif choice == "4":
        print("")
        print("Bye bye!")
        break
    else:
        print("")
        print("Invalid choice")

