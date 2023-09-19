class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def give_raise(self, raise_amount):
    self.salary += raise_amount

  def get_salary(self):
    return self.salary
  


class Company:
  def __init__(self, name):
    self.name = name
    self.employees = []
  

  def hire_employee(self, employee):
    self.employees.append(employee)
  
  def fire_employee(self, employee):
    self.employees.remove(employee)

  def get_total_salary(self):
    total_salary = 0
    for employee in self.employees:
      total_salary += employee.get_salary()
    return total_salary
  

# Create a new company object.
company = Company("J.P. Morgan")

employee1 = Employee("Brian", 100000)
employee2 = Employee("Nick", 90000)
company.hire_employee(employee1)
company.hire_employee(employee2)

employee1.give_raise(10000)
employee2.give_raise(12000)

total_salary = company.get_total_salary()
print(total_salary)





