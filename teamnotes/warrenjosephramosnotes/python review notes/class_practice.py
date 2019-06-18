""" Practice with Classes """

class Employee:

    # Class variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company name'

        # Increments the class variable by 1
        Employee.num_of_emps += 1

    def fullname(self):
        """ The full name of the Employee """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Uses the raise_amt class variable
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # Creates a new Employee
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True

# Create two employee instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# These methods do the same thing (Prints out the first employee's name)
print(Employee.fullname(emp_1))
print(emp_1.fullname())

print("This prints out the employee's pay before and after the raise")
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Prints out the namespace
print(emp_1.__dict__)

# Prints out the number of employees
print("There are " + str(Employee.num_of_emps) + " employees.")

# Raises class variable using a class method (Same thing as Employee.raise_amt = 1.05)
# You can also pass in an instance instead of the class (emp_1.set_raise_amt(1.05))
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))