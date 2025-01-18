class Bank:
    def __init__(self,name,balance):
         self.name = name
         self.balance =  balance
           
    def deposit(self,deposit_amount):
         print("Hello Mr/Mrs",self.name)
         self.balance += deposit_amount
         print(f"Amount {deposit_amount}Rs credit successfully")
         print(f"Your Total Balance {self.balance}")
         
    def withdraw(self,withdraw_amount):
         print("Hello Mr/Mrs",self.name)
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
b.withdraw(6000)
print(b.getBalance())
b.display()
         