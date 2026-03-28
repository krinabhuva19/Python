class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.__emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary
        

    def get_salary(self):
        return self.__salary

    def get_emp_id(self):
        return self.__emp_id

    def display(self):
        print(f"ID: {self.__emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def display(self):   
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, language):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def display(self):      
        super().display()
        print(f"Language: {self.language}")


employees = []

while True:
    print("\n1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Show Details")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        employees.append(Employee(id, name, age, salary))

    elif ch == "2":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        dept = input("Enter Department: ")
        employees.append(Manager(id, name, age, salary, dept))

    elif ch == "3":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        lang = input("Enter Language: ")
        employees.append(Developer(id, name, age, salary, lang))

    elif ch == "4":
        for emp in employees:
            emp.display()
            print("-----------")

    elif ch == "5":
        print("Exiting the system. All resources hve been freed./nGood BYY")

    else:
        print("Invalid choice")
