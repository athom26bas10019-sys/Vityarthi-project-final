#employee details
def display():
    

    print(" EMPLOYEE DETAILS")
    
    

    if len(employees) == 0:
        print("No employees found.")
        return

    for emp in employees:
        print("Employee ID   :", emp["id"])
        print("Name          :", emp["name"])
        print("Department    :", emp["department"])
        print("Designation   :", emp["designation"])
        print("Basic Salary  :", emp["salary"])
        print("Attendance    :", emp["attendance"])
        print("Leave Taken   :", emp["leave"])
