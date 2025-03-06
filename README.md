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
Indentation Issue: The function body was not properly indented, making it invalid Python code.
Readability: The lack of indentation made the structure harder to follow.
Maintainability: Without proper formatting, future modifications could introduce errors.

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
-Indentation corrected for the function body.
-Improved readability and maintainability.
-No changes to logic—calculations remain the same.

Technical Debt Report

1. Technical Debt Identified
Before the refactoring, the following technical debt was present:

Code Formatting Issues: Incorrect indentation made the function invalid.
Readability Concerns: Lack of proper structure made it harder to understand.
Maintainability Risk: Any further modifications could introduce errors due to improper formatting.


2. Refactoring Improvements Made
Applied correct indentation to ensure the script runs without syntax errors.
Improved readability so that future modifications and debugging are easier.
No unnecessary code changes, ensuring the script remains functionally the same.


3. Challenges Faced & Solutions
Challenge	Solution
Indentation errors causing the script to be unreadable	Applied proper indentation to function blocks
Ensuring readability without modifying logic	Focused only on formatting and structure
Avoiding accidental changes in salary deduction calculations	Verified that all formulas and values remained the same
How to Use
Run the script in a Python environment (such as VS Code, PyCharm, or a terminal).
When prompted, enter your monthly salary (e.g., 45000).
The script will display:
Gross salary
Individual deductions (SSS, PhilHealth, Pag-IBIG, Tax)
Total deductions
Net salary (after deductions)

