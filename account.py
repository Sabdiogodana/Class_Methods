class Account:
          def __init__(self,account_name,account_number,):
                 self.account_name = account_name
                 self.account_number = account_number
                 self.balance = 0
                 self.deposits = []
                 self.withdrawals = []                 
                 
          def deposit(self,amount):
              self.balance += amount
              if amount <=0:
                return f"Deposit must be a positive number"
              else:
                self.deposits.append(amount)
                return f"Your current balance is {self.balance} and your deposits are {self.deposits}"

          def withdraw(self,amount):
              self.transaction= 100
              if amount <=0:
                return f"Withdraw must be greater than zero"
              elif amount >self.balance:
                return f"Your balance is{self.balance}, you can't withdraw {amount}"
              else:
                self.withdrawals.append(amount)
                self.balance -= amount + self.transaction
                return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrwals are {self.withdrawals}"

          def deposits_statement(self):
            for amount in self.deposits:
              print(amount,end="\n")

          def withdrawals_statement(self):
            for x in self.deposits:
              print(x ,end="\n")

          def current_balance(self):
             return self.balance

