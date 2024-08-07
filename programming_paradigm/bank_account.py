class BankAccount:
   def __init__(self, initial_balance=0):
      self.__account_balance = initial_balance
   def deposit(self, amount):
      self.__account_balance += amount
      return self.__account_balance += amount
   def withdraw(self, amount):  
          if amount < self.__account_balance:
             self.__account_balance -= amount
      return True
  else:
      return False
      self.__account_balance -= amount  
      print(f"Withdrew: ${amount:.2f}")  
      return True
   def display_balance(self):  
      print(f"Current Balance: ${self.__account_balance:.2f}")
import sys
from bank_account import BankAccount
def main():
   if len(sys.argv) &lt; 2:
      print("Usage: python main-0.py  [amount]")
      return
   command = sys.argv  
   account = BankAccount()  
   if command == "deposit":  
      if len(sys.argv)!= 3:
        print("Usage: python main-0.py deposit ")
        return
      amount = float(sys.argv)  
      account.deposit(amount)
   elif command == "withdraw":
      if len(sys.argv)!= 3:
        print("Usage: python main-0.py withdraw ")
        return
      amount = float(sys.argv)
      account.withdraw(amount) 
   elif command == "display": 
      account.display_balance()
   else:
      print("Invalid command. Supported commands: deposit, withdraw, display")
if __name__ == "__main__":
   main()
