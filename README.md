# Office Management System

## 1. Project Overview

Office Management System is a simple Python based, menu driven

program to manage the details of employees in an office.

The program stores employee details such as Employee ID, name,

department, designation, basic salary, attendance, and leave. It also

provides options to search, update, delete employee records, mark

attendance, apply for leave, and calculate salary.

This project is designed as a simple beginner level Python project using

basic concepts such as functions, lists, dictionaries, loops,

conditions, user input, and exception handling.

## 2. Features

-  Add a new employee

-  Display all employee details

-  Search for an employee using Employee ID

-  Update employee name, department, designation, or salary

-  Delete an employee

-  Mark employee attendance

-  Apply for employee leave

-  Calculate salary

-  Basic Salary

-  HRA (20% of basic salary)

-  DA (10% of basic salary)

-  Gross Salary

-  Tax (10% of gross salary)

-  Net Salary

-  Menu-driven interface

-  Basic validation for salary and leave input

-  Exit option

## 3. Technologies / Tools Used

-  Programming Language: Python

-  Data Structures: List and Dictionary

-  Concepts Used: Functions, loops, conditional statements,

input/output, exception handling

-  Tool/Editor: Any Python supported editor such as VS Code, IDLE,

or PyCharm

-  Python Version: Python 3.x

## 4. Project Files

-  `Vityarthi proj.py` - Main Python program

-  `README.md` - Project documentation

-  `statement.md` - Project problem statement and scope

## 5. Steps to Install & Run the Project

### Step 1: Install Python

Install Python 3.x on your computer if it is not already installed.

### Step 2: Open the Project

Open the Python file `Vityarthi proj.py` in VS Code, IDLE, PyCharm, or

another Python editor.

### Step 3: Run the Program

Run the Python file.

For example, from the terminal:

``` bash

python "Vityarthi proj.py"

```

### Step 4: Use the Menu

After running the program, the following menu is displayed:

``` text

OFFICE MANAGEMENT SYSTEM

1. Add Employee

2. Display Employees

3. Search Employee

4. Update Employee

5. Delete Employee

6. Mark Attendance

7. Apply Leave

8. Calculate Salary

9. Exit

```

Enter the number of the operation you want to perform.

## 6. Instructions for Testing

The following test cases can be used to check the main features.

### Test 1: Add Employee

1. Select option `1`.

2. Enter an Employee ID.

3. Enter the employee name.

4. Enter the department.

5. Enter the designation.

6. Enter a valid basic salary.

7. Check that `Employee added successfully!` is displayed.

### Test 2: Display Employees

1. Select option `2`.

2. Check that the added employee's ID, name, department, designation,

salary, attendance, and leave are displayed.

### Test 3: Search Employee

1. Select option `3`.

2. Enter the Employee ID of an existing employee.

3. Check that the employee details are displayed.

4. Try an ID that does not exist and check that `Employee not found.`

is displayed.

### Test 4: Update Employee

1. Select option `4`.

2. Enter an existing Employee ID.

3. Select one of the update options.

4. Enter the new information.

5. Display the employees again to confirm the change.

### Test 5: Delete Employee

1. Select option `5`.

2. Enter an existing Employee ID.

3. Check that `Employee deleted successfully!` is displayed.

4. Use the display option to confirm that the employee has been

removed.

### Test 6: Attendance

1. Select option `6`.

2. Enter an existing Employee ID.

3. Check that attendance is increased by 1.

### Test 7: Leave

1. Select option `7`.

2. Enter an existing Employee ID.

3. Enter a positive number of leave days.

4. Check that the leave count is updated.

### Test 8: Salary Calculation

1. Select option `8`.

2. Enter an existing Employee ID.

3. Check the displayed basic salary, HRA, DA, gross salary, tax, and

net salary.

### Test 9: Exit

Select option `9` and check that the program displays `Exit!` and stops.

## 7. Screenshots

Screenshots can be added here to show:

-  Main menu

-  Adding an employee

-  Displaying employee details

-  Salary calculation

-  Successful update/delete operations