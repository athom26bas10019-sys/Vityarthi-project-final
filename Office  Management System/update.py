# updated employee details
def update():
    print(" UPDATE EMPLOYEE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            print("\n1. Update Name")
            print("2. Update Department")
            print("3. Update Designation")
            print("4. Update Salary")

            choice = input("Enter your choice: ")

            if choice == "1":
                emp["name"] = input("Enter new name: ")

            elif choice == "2":
                emp["department"] = input("Enter new department: ")

            elif choice == "3":
                emp["designation"] = input("Enter new designation: ")

            elif choice == "4":
                try:
                    emp["salary"] = float(input("Enter new salary: "))
                except ValueError:
                    print("Invalid salary.")
                    return

            else:
                print("Invalid choice.")
                return

            print("Employee updated successfully!")
            return

    print("Employee not found.")