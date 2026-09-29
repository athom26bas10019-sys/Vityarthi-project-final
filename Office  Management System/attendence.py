# attendence
def attendance():
    print("ATTENDANCE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            emp["attendance"] = emp["attendance"] + 1
            print("Attendance marked successfully!")
            return

    print("Employee not found.")