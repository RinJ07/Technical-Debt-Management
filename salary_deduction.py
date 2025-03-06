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
