# Step 1 : Plan the Data Storage

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
}

# Step 2 : Define the Menu System

def main_menu():
    while True:
        print("\n===== Employee Management System (EMS) =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System (EMS). Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Step 3 : Add employee function Functionality

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print(f"Employee {name} added successfully!")

    except ValueError:
        print("Invalid input. Please enter correct data types.")

# Step 4 : View all employees
def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n{:<10} {:<15} {:<5} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, info in employees.items():
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(emp_id, info['name'], info['age'], info['department'], info['salary']))

# Step 5 - Search employee by ID

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            info = employees[emp_id]
            print(f"\nDetails for Employee ID {emp_id}:")
            print(f"Name      : {info['name']}")
            print(f"Age       : {info['age']}")
            print(f"Department: {info['department']}")
            print(f"Salary    : {info['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a valid Employee ID.")

# Run the program
if __name__ == "__main__":
    main_menu()
