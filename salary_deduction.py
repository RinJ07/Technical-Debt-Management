class SalaryCalculator:
    def __init__(self, salary):
        try:
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")

            self.salary = salary
            self.sss = self.compute_sss()
            self.philhealth = self.compute_philhealth()
            self.pagibig = self.compute_pagibig()
            self.tax = self.compute_tax()  # Tax should be based on taxable income

        except ValueError as e:
            print(f"Error: {e}")
            raise

    def compute_sss(self):
        """Computes SSS contribution based on provided salary brackets."""
        try:
            sss_table = [
                (5000, 250), (5500, 275), (6000, 300), (6500, 325), (7000, 350),
                (7500, 375), (8000, 400), (8500, 425), (9000, 450), (9500, 475),
                (10000, 500), (10500, 525), (11000, 550), (11500, 575), (12000, 600),
                (12500, 625), (13000, 650), (13500, 675), (14000, 700), (14500, 725),
                (15000, 750), (15500, 775), (16000, 800), (16500, 825), (17000, 850),
                (17500, 875), (18000, 900), (18500, 925), (19000, 950), (19500, 975),
                (20000, 1000), (20500, 1025), (21000, 1050), (21500, 1075), (22000, 1100),
                (22500, 1125), (23000, 1150), (23500, 1175), (24000, 1200), (24500, 1225),
                (25000, 1250), (25500, 1275), (26000, 1300), (26500, 1325), (27000, 1350)
            ]
            for limit, contrib in sss_table:
                if self.salary <= limit:
                    return contrib
            return 1350  # Updated max contribution

        except Exception as e:
            print(f"Error in computing SSS: {e}")
            return 1350  # Fallback value

    def compute_philhealth(self):
        """Computes PhilHealth contribution based on 5% rate (shared by employer and employee)."""
        try:
            return min(2500, max(500, self.salary * 0.05)) / 2  # Cap at 2500 (employee share)
        except Exception as e:
            print(f"Error in computing PhilHealth: {e}")
            return 500  # Fallback value

    def compute_pagibig(self):
        """Computes Pag-IBIG contribution (2% for employees, max PHP 100)."""
        try:
            return min(100, self.salary * 0.02)
        except Exception as e:
            print(f"Error in computing Pag-IBIG: {e}")
            return 100  # Fallback value

    def compute_tax(self):
        """Computes tax based on taxable income (Gross Salary - Mandatory Contributions)."""
        try:
            taxable_income = self.salary - (self.sss + self.philhealth + self.pagibig)

            if taxable_income <= 20833:
                return 0
            elif taxable_income <= 33333:
                return (taxable_income - 20833) * 0.2
            elif taxable_income <= 66667:
                return 2500 + (taxable_income - 33333) * 0.25
            elif taxable_income <= 166667:
                return 10833 + (taxable_income - 66667) * 0.3
            else:
                return 40833 + (taxable_income - 166667) * 0.35

        except Exception as e:
            print(f"Error in computing tax: {e}")
            return 0  # Fallback value

    def compute_total_deductions(self):
        try:
            return self.sss + self.philhealth + self.pagibig + self.tax
        except Exception as e:
            print(f"Error in computing total deductions: {e}")
            return 0  # Fallback value

    def compute_net_salary(self):
        try:
            return self.salary - self.compute_total_deductions()
        except Exception as e:
            print(f"Error in computing net salary: {e}")
            return self.salary  # Fallback value

    def get_summary(self):
        try:
            return (
                f"Gross Salary: {self.salary}\n"
                f"SSS Deduction: {self.sss}\n"
                f"PhilHealth Deduction: {self.philhealth}\n"
                f"Pag-IBIG Deduction: {self.pagibig}\n"
                f"Tax Deduction: {self.tax}\n"
                f"Total Deductions: {self.compute_total_deductions()}\n"
                f"Net Salary: {self.compute_net_salary()}"
            )
        except Exception as e:
            return f"Error in generating summary: {e}"


def get_valid_salary():
    """Prompts the user to input their salary and ensures valid numeric input."""
    while True:
        try:
            salary = float(input("Enter your salary amount: "))
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")
            return salary
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")


if __name__ == "__main__":
    try:
        salary = get_valid_salary()
        calculator = SalaryCalculator(salary)
        print(calculator.get_summary())
    except Exception as e:
        print(f"Program encountered an error: {e}. Please restart and try again.")
