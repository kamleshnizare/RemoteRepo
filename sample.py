class Bank:
    def __init__(self,name,balance):
         self.name = name
         self.balance =  balance
           
    def deposit(self):
         print("Hello Mr/Mrs",self.name)
         deposit_amount = float(input('Enter the amount'))
         self.balance += deposit_amount
         print(f"Amount {deposit_amount}Rs credit successfully")
         print(f"Your Total Balance {self.balance}")
         
    def withdraw(self):
         print("Hello Mr/Mrs",self.name)
         withdraw_amount = float(input('Enter the amount'))
         if self.balance >= withdraw_amount:
               self.balance -= withdraw_amount
               print(f'Amount {withdraw_amount} debited in your account')
               print(f'Your Total Balance = {self.balance}')
              
    def getBalance(self):
         return self.balance
         
    def display(self):
         print(f"NAME    : {self.name}\
               \nBalance : {self.balance}")
               
b = Bank('KAMLESH',5000)
b.deposit(3000)
b.withdraw()
print(b.getBalance())
b.display()
         
