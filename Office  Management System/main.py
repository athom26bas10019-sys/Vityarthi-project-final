# Main method
while True:

    
    print("       OFFICE MANAGEMENT SYSTEM")
    print(())

    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. Apply Leave")
    print("8. Calculate Salary")
    print("9. Exit")

    choice = input("\nEnter your choice: ")



    if choice == "1":
        print(" add employee")
        add()
        
        print("CHECK AFTER ADD:",employees)

    elif choice == "2":
        display()

       
        

       

    elif choice == "3":
        print("employee search")
        search()

    elif choice == "4":
        print(" UPDATE EMPLOYEE")
        update()

    elif choice == "5":
        print("DELETE EMPLOYEE")
        delete()

    elif choice == "6":
        print("ATTENDANCE")
        attendance()

    elif choice == "7":
        print("APPLY LEAVE")
        apply_leave()

    elif choice == "8":
        print("SALARY CALCULATION ")
        salary()

    elif choice == "9":
        print("Exit!")
        break

    else:
        print("Invalid choice.")

