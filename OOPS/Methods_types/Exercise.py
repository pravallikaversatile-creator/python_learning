class Employee:
    company = "TechCorp"      # class attribute
    employee_count = 0        # class attribute

    def __init__(self, name, salary):
        self.name = name              # instance attribute
        self.salary = salary          # instance attribute
        Employee.employee_count += 1  # update class attribute

    # Instance Method
    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    # Class Method
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # Alternative Constructor (Class Method)
    @classmethod
    def from_string(cls, emp_string):
        name, salary = emp_string.split("-")
        return cls(name, int(salary))

    # Static Method
    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


# ---------------------------
# Using the methods
# ---------------------------

# Using static method
print(Employee.is_valid_salary(50000))   # True

# Creating objects normally
e1 = Employee("Maya", 60000)
e2 = Employee("Arjun", 75000)

# Using instance method
e1.show_details()
e2.show_details()

# Using class method to change class attribute
Employee.change_company("InnoTech")

# After company change
e1.show_details()
e2.show_details()

# Using alternative constructor
e3 = Employee.from_string("Riya-55000")
e3.show_details()

# Total employees
print("Total employees:", Employee.employee_count)

