# salary
def salary():
    print("SALARY CALCULATION ")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            basic = emp["salary"]

            # Allowance
            hra = basic * 0.20
            da = basic * 0.10

            # Total salary
            gross_salary = basic + hra + da

            # Tax
            tax = gross_salary * 0.10

            # Net salary
            net_salary = gross_salary - tax

            print("\nBasic Salary :", basic)
            print("HRA          :", hra)
            print("DA           :", da)
            print("Gross Salary :", gross_salary)
            print("Tax          :", tax)
            print("Net Salary   :", net_salary)

            return

    print("Employee not found.")