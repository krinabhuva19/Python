import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ExpenseDataAnalyzer:

    def __init__(self):
        self.data = None
        self.current_plot = None

    def __del__(self):
        plt.close('all')

    
    def load_data(self, file_path):
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path, parse_dates=['Date'])
        elif file_path.endswith(('.xlsx', '.xls')):
            self.data = pd.read_excel(file_path, parse_dates=['Date'])
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")

        print("Expense Dataset Loaded Successfully!")

    
    def explore_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n===== Explore Expense Data =====")
            print("1. First 5 Rows")
            print("2. Last 5 Rows")
            print("3. Column Names")
            print("4. Data Types")
            print("5. Dataset Info")
            print("6. Back")

            choice = input("Enter choice: ")

            if choice == '1':
                print(self.data.head())

            elif choice == '2':
                print(self.data.tail())

            elif choice == '3':
                print(self.data.columns.tolist())

            elif choice == '4':
                print(self.data.dtypes)

            elif choice == '5':
                self.data.info()

            elif choice == '6':
                break

            else:
                print("Invalid Choice!")

    
    def dataframe_operations(self):

        if self.data is None:
            print("No dataset loaded.")
            return

        while True:

            print("\n===== Expense Operations =====")
            print("1. Expense Calculations")
            print("2. Combine Data")
            print("3. Split By Category")
            print("4. Back")

            choice = input("Enter choice: ")

            if choice == '1':

                arr = self.data['Amount'].dropna().to_numpy()

                print(f"Total Expense : {arr.sum():.2f}")
                print(f"Average Expense : {arr.mean():.2f}")
                print(f"Maximum Expense : {arr.max():.2f}")
                print(f"Minimum Expense : {arr.min():.2f}")

            elif choice == '2':

                combined = pd.concat([self.data, self.data], ignore_index=True)

                print("Original Rows :", len(self.data))
                print("Combined Rows :", len(combined))

            elif choice == '3':

                for cat, grp in self.data.groupby('Category'):

                    print("\nCategory :", cat)
                    print(grp[['Expense_Name', 'Amount']].head())

            elif choice == '4':
                break

            else:
                print("Invalid Choice!")

    
    def handle_missing_data(self):

        if self.data is None:
            print("No dataset loaded.")
            return

        while True:

            print("\n===== Missing Data Handling =====")
            print("1. Show Missing Data")
            print("2. Fill Missing With Mean")
            print("3. Drop Missing Rows")
            print("4. Back")

            choice = input("Enter choice: ")

            if choice == '1':

                print(self.data[self.data.isnull().any(axis=1)])

            elif choice == '2':

                num_cols = self.data.select_dtypes(include=np.number).columns

                self.data[num_cols] = self.data[num_cols].fillna(
                    self.data[num_cols].mean()
                )

                print("Missing values filled successfully!")

            elif choice == '3':

                self.data.dropna(inplace=True)

                print("Missing rows deleted!")

            elif choice == '4':
                break

            else:
                print("Invalid Choice!")

    
    def descriptive_statistics(self):

        if self.data is None:
            print("No dataset loaded.")
            return

        print("\n===== Expense Statistics =====")

        print(self.data.describe())

        pivot = self.data.pivot_table(
            values='Amount',
            index='Category',
            columns='Payment_Mode',
            aggfunc='sum',
            fill_value=0
        )

        print("\nExpense Pivot Table:\n")
        print(pivot)

    
    def visualize_data(self):

        if self.data is None:
            print("No dataset loaded.")
            return

        while True:

            print("\n===== Expense Visualization =====")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Back")

            choice = input("Enter choice: ")

            if choice == '6':
                break

            fig, ax = plt.subplots(figsize=(10, 6))

            if choice == '1':

                grp = self.data.groupby('Category')['Amount'].sum()

                grp.plot(kind='bar', ax=ax)

                ax.set_title("Total Expense By Category")

            elif choice == '2':

                ts = self.data.groupby('Date')['Amount'].sum()

                ts.plot(ax=ax)

                ax.set_title("Expense Over Time")

            elif choice == '3':

                ax.scatter(self.data['Amount'], self.data['Tax'])

                ax.set_xlabel("Amount")
                ax.set_ylabel("Tax")

                ax.set_title("Amount vs Tax")

            elif choice == '4':

                grp = self.data.groupby('Category')['Amount'].sum()

                grp.plot(kind='pie', ax=ax, autopct='%1.1f%%')

                ax.set_ylabel("")

                ax.set_title("Expense Share")

            elif choice == '5':

                self.data['Amount'].plot(kind='hist', bins=20, ax=ax)

                ax.set_title("Expense Distribution")

            else:
                print("Invalid Choice!")
                plt.close()
                continue

            plt.tight_layout()

            self.current_plot = fig

            plt.show()

    
    def save_visualization(self):

        if self.current_plot is None:
            print("No plot available!")
            return

        fname = input("Enter file name : ")

        self.current_plot.savefig(fname)

        print("Visualization Saved Successfully!")

    
    def run(self):

        while True:

            print("\n========== Expense Data Analysis ==========")

            print("1. Load Expense Dataset")
            print("2. Explore Data")
            print("3. DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Descriptive Statistics")
            print("6. Visualization")
            print("7. Save Visualization")
            print("8. Exit")

            choice = input("Enter choice: ")

            if choice == '1':

                path = input("Enter Expense CSV File Path : ")

                try:
                    self.load_data(path)

                except Exception as e:
                    print("Error :", e)

            elif choice == '2':
                self.explore_data()

            elif choice == '3':
                self.dataframe_operations()

            elif choice == '4':
                self.handle_missing_data()

            elif choice == '5':
                self.descriptive_statistics()

            elif choice == '6':
                self.visualize_data()

            elif choice == '7':
                self.save_visualization()

            elif choice == '8':

                print("Program Closed!")
                quit()

            else:
                print("Invalid Choice!")


if __name__ == '__main__':

    analyzer = ExpenseDataAnalyzer()

    analyzer.run()