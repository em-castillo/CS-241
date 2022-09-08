'''Week 07 Team Activity'''

from abc import ABC
from abc import abstractmethod

# abstract parent class


class Employee(ABC):
    def __init__(self):
        self.name = ""

    # prompt for name
    def prompt(self):
        self.name = input("Enter name: ")

    @abstractmethod  # when used this method in parent class is empty
    def display(self):
        pass

    @abstractmethod
    def get_paycheck(self):
        pass

# child class


class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_wage = 0
        self.hours = 0

    # prompt for hourly wage and hours
    def prompt(self):
        super().prompt()
        self.hourly_wage = int(input("Enter hourly wage: "))
        self.hours = int(input("Enter hours worked: "))

    # override display function from parent
    def display(self):
        print(f"{self.name} - ${self.hourly_wage}/hour")

    # override function from parent
    def get_paycheck(self):
        paycheck = self.hourly_wage * self.hours
        return paycheck


# child class
class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 0

    # prompt for salary
    def prompt(self):
        super().prompt()
        self.salary = int(input("Enter salary: "))

    def display(self):
        # override function
        print(f"{self.name} - ${self.salary}/year")

    # override function
    def get_paycheck(self):
        paycheck = self.salary / 24
        return paycheck


# stretch challenge. Regular function
def display_employee_data(person):
    person.display()
    print(f"Paycheck = ${person.get_paycheck():.2f}")


def main():
    # declare list for employees
    employees = []

    option = ""
    # loop
    while option.lower() != "q":
        option = input(
            "Enter h for hourly employee, s for salary employee, or q to quit: ")
        if option.lower() == "h":
            # create a new employee object
            person = HourlyEmployee()
            # prompt
            person.prompt()
            # Add to the List
            employees.append(person)

        elif option.lower() == "s":
            # create a new employee object
            person = SalaryEmployee()
            person.prompt()
            # Add to the List
            employees.append(person)

        elif option.lower() == "q":
            # loop through the list and call the display method for each employee.
            for person in employees:
                display_employee_data(person)


if __name__ == "__main__":
    main()
