# search employee
def search():
    print("employee search")

    emp_id = input("Enter Employee ID: ")

    found = False

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("Name        :", emp["name"])
            print("Department  :", emp["department"])
            print("Designation :", emp["designation"])
            print("Salary      :", emp["salary"])
            found = True
            break

    if found == False:
        print("Employee not found.")
