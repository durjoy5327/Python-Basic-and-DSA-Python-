"""
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
"""
def problem1(month_expenses):
    jan_expense = month_expenses[0]['January']
    feb_expense = month_expenses[1]['February']
    print("In February, the amount of extra money spent:", feb_expense - jan_expense)

def problem2(month_expenses):
    total = month_expenses[0]['January'] + month_expenses[1]['February'] + month_expenses[2]['March']
    print("Total expense in the first quarter (first three months) of the year:", total)

def problem3(month_expenses, amount):
    
    for month_expense in month_expenses:
        for month, expense in month_expense.items():
            if expense == amount:
                print(f"You spent {amount} dollars in {month} month")
                return
    print(f"You didn't spend {amount} dollars in any month")

def add_month(month_expenses, month, money):
    month_expenses.append({month: money})
    print(month_expenses)

def change_expense(month_expenses, month, refund):
    for month_expense in month_expenses:
        if month in month_expense:
            month_expense[month] -= refund
            print(f"After refunding, the expense of {month} is {month_expense[month]}")
            break

# List of dictionaries to store monthly expenses
month_expenses = [
    {'January': 2200},
    {'February': 2350},
    {'March': 2600},
    {'April': 2130},
    {'May': 2190}
]

problem1(month_expenses)
problem2(month_expenses)
problem3(month_expenses, 2200)
add_month(month_expenses, 'June', 1980)
change_expense(month_expenses, 'April', 200)