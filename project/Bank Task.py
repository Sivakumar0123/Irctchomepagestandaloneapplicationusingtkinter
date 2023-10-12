import datetime


class Bank_passbook:
    def __init__(self):
        self.transaction=[]
        self.opening_balance=10000
    def credit(self):
        count =int(input('Enter the amount to be Deposited:'))
        count+=self.opening_balance
        self.opening_balance=count
        time = datetime.datetime.now()
        self.transaction.append(['Cr',count,time])
    def deposit(self):
        Withdrawn=int(input('Enter the amount to be Withdrwan:'))
        time = datetime.datetime.now()
        self.opening_balance-=Withdrawn
        self.transaction.append(['Dr',Withdrawn,time])
    def challan(self):
         print('********************************************************************************')
         print('                 INDIAN OVERSEAS BANK - PASS BOOK DETAILS'                       )
         print('********************************************************************************')
         print('Opening balance:', 10000)
         print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
         print('status     credit        debit       total       time')
         print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

         
         total_balance = self.opening_balance
         for types,amount,time in self.transaction:
            if types == 'Cr':
                total_balance += amount
                print(f' {types}         {amount}        -       {total_balance}         {time}')
            else:
                total_balance -= amount
                print(f' {types}           -        {amount}     {total_balance}         {time}')
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

b = Bank_passbook()

transection=int(input('Enter the choice for the transection:'))
for i in range(transection):              
    print('-------------------------------------------------------')
    print('           Welcome to Indian Overseas Bank')
    print('-------------------------------------------------------')
    print(f'Enter the choice for transection: {i+1}')
    op=int(input('type:(1.Credit | 2.Debit):'))
    if op == 1:
        b.credit()
    elif op == 2:
        b.deposit()
    else:
        quit()

b.challan()
