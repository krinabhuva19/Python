import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ExpenseTracker:

    def __init__(self, file):
        self.file = file
        try:
            self.df = pd.read_csv(file)
        except:
            self.df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])

    def add_expense(self, date, amount, category, description):
        if amount <= 0:
            print("Invalid amount!")
            return
        
        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        self.df.to_csv(self.file, index=False)
        print("Expense added successfully!")


    def get_summary(self):
        if self.df.empty:
            print("No data available")
            return

        total = np.sum(self.df["Amount"])
        avg = np.mean(self.df["Amount"])

        print("\nTotal Expense:", total)
        print("Average Expense:", avg)

  
    def filter_expenses(self, category=None):
        if category:
            filtered = self.df[self.df["Category"] == category]
        else:
            filtered = self.df

        print(filtered)

   
    def generate_report(self):
        print("\nExpense by Category:")
        print(self.df.groupby("Category")["Amount"].sum())

  
    def visualize(self):
        if self.df.empty:
            print("No data to visualize")
            return

        self.df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Total Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

        self.df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.show()

        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df.sort_values("Date", inplace=True)
        plt.plot(self.df["Date"], self.df["Amount"])
        plt.title("Expense Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()

        plt.hist(self.df["Amount"])
        plt.title("Expense Frequency")
        plt.xlabel("Amount")
        plt.ylabel("Frequency")
        plt.show()


# ================= MENU =================

def menu():
    tracker = ExpenseTracker("expenses.csv")

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter by Category")
        print("4. Generate Report")
        print("5. Visualization")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            desc = input("Enter Description: ")
            tracker.add_expense(date, amount, category, desc)

        elif ch == "2":
            tracker.get_summary()

        elif ch == "3":
            cat = input("Enter category: ")
            tracker.filter_expenses(cat)

        elif ch == "4":
            tracker.generate_report()

        elif ch == "5":
            tracker.visualize()

        elif ch == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


menu()