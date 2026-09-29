
# add employee
def add():
    
    
   

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")

    try:
        salary = float(input("Enter Basic Salary: "))
    except ValueError:
        print("Invalid salary!")
        return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "designation": designation,
        "salary": salary,
        "attendance": 0,
        "leave": 0
    }

    employees.append(employee)
    

    print("Employee added successfully!")