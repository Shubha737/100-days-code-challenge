# Understanding_classes_and_instances

class Employee:
    pass

emp_1 = Employee()
print(emp_1)
emp_2 = Employee()
print(emp_2)

emp_1.first = 'Corey'
emp_1.lasr = 'Schafer'
emp_1.mail = 'coreyschafer@gmail.com'
emp_1.pay = 50000

print(emp_1.mail)