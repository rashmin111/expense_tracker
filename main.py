import csv
from datetime import datetime


def add_transaction():
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")
    date = datetime.now().strftime("%Y-%m-%d")
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])


def view_summary():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


while True:
    choice = input("1: Add, 2: View, 3: Quit > ")
    if choice == '1':
        add_transaction()
    elif choice == '2':
        view_summary()
    else:
        break
