''' add employee, view employee, remove employee, exit employee '''

class Employee:
    def add_employee(self):
        self.emp = []
        count = int(input('enter the no of employees'))
        print('enter the names:')
        for i in range(count):
            ename = input()
            self.emp.append(ename)
    def view_employee(self):
        for sno , name in enumerate(self.emp,1):
            print('{}.{}'.format(sno,name))
    def remove_employee(self):
        name  = input('enter the eployees')
        if name in self.emp:
            self.emp.remove(name)
            print('removed employees')
        else:
            print('name is not exist')

e = Employee()

while True:
    print('\n1.add employee \n2.view employee \n3.remove employee \n4.exit employee')
    op = int(input('enter the operation :'))
    if op == 1:
        e.add_employee()
    elif op == 2:
        e.view_employee()
    elif op == 3:
        e.remove_employee()
    else:
        quit()
        
    
    
