class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id:<10} {self.name:<10} {self.age:<5} {self.salary:<10}"


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, parameter):
        if parameter == 1:
            self.employees.sort(key=lambda x: x.age)
        elif parameter == 2:
            self.employees.sort(key=lambda x: x.name)
        elif parameter == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid parameter choice")

    def display_employees(self):
        header = f"{'Employee ID':<10} {'Name':<10} {'Age':<5} {'Salary (PM)':<10}"
        print(header)
        print("=" * len(header))
        for employee in self.employees:
            print(employee)


# Create instances of Employee and add them to the EmployeeTable
employee_table = EmployeeTable()
employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
employee_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

# Get user input for sorting parameter
print("Choose a sorting parameter:")
print("1. Sort by Age")
print("2. Sort by Name")
print("3. Sort by Salary")
choice = int(input("Enter your choice: "))

# Sort and display the data based on the user's choice
employee_table.sort_employees(choice)
print("\nSorted Employee Data:")
employee_table.display_employees()
