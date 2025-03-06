**Technical Debt Management and Salary Deduction Calculator**

## Overview
This project involves a Salary Deduction Calculator program that computes deductions based on predefined values for SSS, PhilHealth, Pag-IBIG, and tax. After calculating the deductions, the program displays the net salary of an employee.

## How It Works
1. **User Input:** The user inputs their monthly salary when prompted.
2. **Deduction Calculations:**
   - **SSS:** A fixed deduction of ₱1,200.
   - **PhilHealth:** Computed as 5% of the salary, divided by 2 (assuming employer and employee share the cost).
   - **Pag-IBIG:** A fixed deduction of ₱100.
   - **Tax:** A fixed deduction of ₱1,875 (for simplicity, without progressive tax calculations).
3. **Total Deductions:** The script computes the total of the deductions and subtracts them from the gross salary.
4. **Net Salary:** Displays a breakdown of the deductions and the net salary after applying all deductions.

## Modified Code
The following code refactors the initial procedural approach into an object-oriented approach (OOP) to improve modularity, flexibility, and maintainability.

```python
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
```

## Technical Debt Management
### Technical Debt Identified
1. **Poor Readability:**
   - The original code contained unclear variable names and formatting issues that made the logic harder to understand.
2. **Hardcoded Values:**
   - The script used fixed values for deductions, limiting flexibility. Future changes to deduction amounts would require modifying the code directly.
3. **Lack of Modular Functions:**
   - The logic for computing deductions, printing results, and handling user input was all mixed together, making maintenance difficult.
4. **No Input Validation:**
   - The original script did not handle invalid or non-numeric salary inputs, leading to potential runtime errors.

### Refactoring Improvements Made
1. **Object-Oriented Programming (OOP) Approach:**
   - The refactored code uses a `SalaryCalculator` class, encapsulating logic for computing deductions and displaying results, promoting reusability.
2. **Improved Code Readability:**
   - Variables are more descriptive, improving clarity and understanding.
3. **Modular Functions:**
   - The code was divided into smaller methods:
     - `compute_philhealth()`
     - `compute_total_deductions()`
     - `compute_net_salary()`
   - This makes the code easier to modify and extend.
4. **Input Validation:**
   - The `get_valid_salary()` function ensures the user enters a positive number, preventing errors.
5. **Error Handling:**
   - Exception handling ensures robustness against invalid inputs.

## Challenges Faced & Solutions
| Challenge | Solution |
|-----------|----------|
| Hardcoded values reducing flexibility | Moved to an OOP design, making values easier to update |
| No input validation causing errors | Introduced `get_valid_salary()` to validate user input |
| Lack of modularity making updates difficult | Split logic into smaller methods for better maintainability |

## Testing
### Testing Strategy
- **Manual Testing:** Verified correct input validation and deduction calculations.
- **Unit Testing:** Automated test cases validated core functionality.

### Test Cases
1. **Valid Salary Input**
   - **Test Case:** User inputs a valid salary (e.g., ₱50,000).
   - **Expected Output:**
     ```
     Gross Salary: ₱50,000
     SSS Deduction: ₱1,200
     PhilHealth Deduction: ₱1,250
     Pag-IBIG Deduction: ₱100
     Tax Deduction: ₱1,875
     Total Deductions: ₱4,425
     Net Salary: ₱45,575
     ```
2. **Invalid Salary Input (Non-numeric Input)**
   - **Test Case:** User enters "abc".
   - **Expected Output:** Error message prompting for valid input.
3. **Invalid Salary Input (Negative Salary)**
   - **Test Case:** User enters a negative salary.
   - **Expected Output:** Error message prompting for valid input.
4. **Edge Case (Large Salary)**
   - **Test Case:** User enters ₱1,000,000.
   - **Expected Output:** Correct deductions and net salary calculation.

### Test Coverage
- **Input Validation:** Tested multiple invalid inputs.
- **Salary Deduction Calculations:** Verified correctness of deductions.
- **Edge Cases:** Ensured handling of both small and large salaries.

## Conclusion
By refactoring the initial code, we have:
- Improved readability with clear variable names and structure.
- Increased modularity with smaller, reusable functions.
- Enhanced robustness through input validation and error handling.
- Verified functionality through manual and automated testing.

This refactor makes the program more maintainable and adaptable for future enhancements.

