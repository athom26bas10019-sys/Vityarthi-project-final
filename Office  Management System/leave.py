# apply for leave
def apply_leave():
    print("APPLY LEAVE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            try:
                days = int(input("Enter number of leave days: "))
            except ValueError:
                print("Please enter a valid number.")
                return

            if days > 0:
                emp["leave"] = emp["leave"] + days
                print("Leave applied successfully!")
            else:
                print("Invalid number of days.")

            return

    print("Employee not found.")