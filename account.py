class Account:
          def __init__(self,name,account_name,account_number,balance):
                 self.name = name
                 self.account_name = account_name
                 self.account_number = account_number
                 self.balance = balance
                 
                 
          def deposit(self,amount):
              self.balance += amount
              return f"Your current balance is {self.balance}"

          def withdraw(self,amount):
              self.balance -= amount
              return f"Your current balance is {self.balance}"
           