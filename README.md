# Technical-Debt-Management
Salary Deduction Calculator
This script is designed to compute salary deductions based on predefined values for SSS, PhilHealth, Pag-IBIG, and tax. After deducting these values, it calculates and displays the net salary of an employee.

How It Works
The user inputs their monthly salary when prompted.
The script deducts the following amounts:
SSS: A fixed deduction of ₱1,200.
PhilHealth: Computed as 5% of the salary, divided by 2 (assuming employer and employee share the cost).
Pag-IBIG: A fixed deduction of ₱100.
Tax: A fixed deduction of ₱1,875 (for simplicity, without progressive tax calculations).
The script calculates the total deductions and subtracts them from the gross salary.
Finally, it displays a breakdown of the deductions and the net salary after all deductions are applied.

Updates in the Modified Code
Fixed Formatting and Readability:
Proper indentation: The original function lacked proper indentation, which could lead to errors or make the code harder to read.
No changes to computation logic: The way deductions are calculated remains exactly the same.
Original Code (Before Formatting Fix)
Below is the original, unformatted code, which contained incorrect indentation in the function definition.

def compute_deductions(salary):
sss = 1200
philhealth = (salary * 0.05) / 2
pagibig = 100
tax = 1875 # Assuming fixed value for simplicity

deductions = sss + philhealth + pagibig + tax
net_salary = salary - deductions

print("Gross Salary:", salary)
print("SSS Deduction:", sss)
print("PhilHealth Deduction:", philhealth)
print("Pag-IBIG Deduction:", pagibig)
print("Tax Deduction:", tax)
print("Total Deductions:", deductions)
print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)

Problems with the Original Code
The function body lacks indentation, which is required in Python. Without proper indentation, the script might not run properly.
Readability is affected, making it harder to understand the structure of the function.

Modified Code (After Formatting Fix)
In this version, proper indentation is applied, ensuring that the function is correctly structured and easy to read.

def compute_deductions(salary):
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875  # Assuming fixed value for simplicity

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)

Key Fixes in the Modified Code
Proper indentation applied to all lines within the function.
Improved readability for future modifications or debugging.
No changes to logic, ensuring the script still calculates deductions correctly.
