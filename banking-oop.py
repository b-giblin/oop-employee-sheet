class Bank:
  def __init__(self, account_number, balance, account_type):
    self.account_number = account_number
    self.balance = balance
    self.account_type = account_type
  

  def deposit(self, amount):
    self.balance += amount

  
  def withdraw(self, amount):
    if amount > self.balance:
      raise ValueError("Insuficient funds")
    else:
      self.balance -= amount


  def get_balance(self):
    return self.balance

  def get_account_type(self):
    return self.account_number


# Create bank account object.
bank_account = Bank(12343, 75000, "Checking")


# deposit 500$
bank_account.deposit(500)

# Withdraw $200 from the account
bank_account.withdraw(200)

# Get the balance of the account
balance = bank_account.get_balance()
type = bank_account.get_account_type()
print(balance)

print(type)