# Task Nr.4:

# Create a class called Employee with a static method called calculate_payroll that takes a list of Employee
# instances and returns the total amount to be paid to all employees. Each Employee instance has two attributes:
# name and salary.

from typing import List


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employee_list: List["Employee"]) -> float:
        # return sum(emplyee.salary for emplyee in employee_list)

        summed_salaries = 0.0
        for employee in employee_list:
            summed_salaries += employee.salary
        return summed_salaries


employee_list = [
    Employee(name="Antanas", salary=1000),
    Employee(name="Petras", salary=1500),
    Employee(name="Direktorius", salary=2500),
]
print(Employee.calculate_payroll(employee_list=employee_list))
