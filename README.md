# Technical-Debt-Management
Salary Deduction Calculator
This program computes salary deductions based on predefined values for SSS, PhilHealth, Pag-IBIG, and tax. After deducting these values, it calculates and displays the net salary of an employee.

How It Works
1.The user inputs their monthly salary when prompted.
2.The script deducts the following amounts:

  -SSS: A fixed deduction of ₱1,200.
  -PhilHealth: Computed as 5% of the salary, divided by 2 (assuming employer and employee share the cost).
  -Pag-IBIG: A fixed deduction of ₱100.
  -Tax: A fixed deduction of ₱1,875 (for simplicity, without progressive tax calculations).

3.The script calculates the total deductions and subtracts them from the gross salary.
4.It then displays a breakdown of the deductions and the net salary after all deductions are applied.

Modified Code

class SalaryCalculator:
    def __init__(self, salary):
        self.salary = salary
        self.sss = 1200
        self.pagibig = 100
        self.tax = 1875

    def compute_philhealth(self):
        return (self.salary * 0.05) / 2

    def compute_total_deductions(self):
        return self.sss + self.compute_philhealth() + self.pagibig + self.tax

    def compute_net_salary(self):
        return self.salary - self.compute_total_deductions()

    def display_summary(self):
        print(f"Gross Salary: {self.salary}")
        print(f"SSS Deduction: {self.sss}")
        print(f"PhilHealth Deduction: {self.compute_philhealth()}")
        print(f"Pag-IBIG Deduction: {self.pagibig}")
        print(f"Tax Deduction: {self.tax}")
        print(f"Total Deductions: {self.compute_total_deductions()}")
        print(f"Net Salary: {self.compute_net_salary()}")

def get_valid_salary():
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")
            return salary
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid salary.")

salary = get_valid_salary()
calculator = SalaryCalculator(salary)
calculator.display_summary()

Technical Debt Report

Technical Debt Identified:

  -Poor Readability: The original function had unclear variable names and formatting issues.
  -Hardcoded Values: The script used fixed values for deductions without flexibility for updates.
  -Lack of Modular Functions: All logic was inside a single function, making it harder to modify.
  -No Input Validation: The script did not check for invalid or negative salary inputs.

Refactoring Improvements Made:

  -Converted to an OOP approach to enhance reusability and scalability.
  -Improved code readability with clear variable names and structured formatting.
  -Implemented modular functions for better maintainability.
  -Added input validation to prevent invalid inputs.
  -Ensured calculations remain correct while making the code more adaptable.

Challenges Faced & Solutions:

Challenge:
  -Hardcoded values reducing flexibility
  -No input validation causing errors
  -Lack of modularity making updates difficult

Solution:
  -Used functions and class-based approach for adaptability.
  -Implemented a loop to handle invalid salary inputs.
  -Divided logic into functions for easy modification.



