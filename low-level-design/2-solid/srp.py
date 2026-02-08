# Single Responsibility Principle

# Voilation of Single Responsibility Principle
# Actually, there is NO violation of the Single Responsibility Principle here.
# Both SalaryCalculator and ReportGenerator have only one responsibility each.
# SalaryCalculator only calculates salaries, and ReportGenerator only generates reports.
# A violation WOULD look like this (for illustration):

class SalaryCalculatorVoilation:
    def calculate_salary(self, hours_worked, hourly_rate):
        # Calculates salary
        return hours_worked * hourly_rate

    def generate_report(self, salary):
        # This method violates SRP, because salary calculation and reporting
        # are two separate concerns.
        print(f"Salary report: {salary}")

# In the shown code, each class has a single responsibility.

# Solution for Single Responsibility Principle
class SalaryCalculator:
    def __init__(self):
        self.salary = 0

    def calculate_salary(self, hours_worked, hourly_rate):
        pass

class ReportGenerator:
    def generate_report(self, salary):
        pass

if __name__ == "__main__":
    salaryCalculatorVoilation = SalaryCalculatorVoilation()
    salaryCalculatorVoilation.calculate_salary(10, 100)

    salaryCalculator = SalaryCalculator()
    salaryCalculator.calculate_salary(10, 100)

    reportGenerator = ReportGenerator()
    reportGenerator.generate_report(1000)