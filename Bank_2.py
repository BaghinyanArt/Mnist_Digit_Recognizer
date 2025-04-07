class InsufficientFundsError(Exception):
    pass

class BankAccount():  
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("You can't deposite that much money. Sorry!\n")
            raise ValueError
        else: 
            return self.balance + amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough money in your balance!\n")
            raise InsufficientFundsError
        elif amount < 0:
            print("You can't withdraw that much money. Sorry!\n")
            raise ValueError
        else:
            return self.balance - amount
        
class Bank():
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print("Account already exists!")
            raise ValueError
        else:
            self.accounts[account.account_number] = account
            print("Account added!")  

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts:
            print("Account didn't find!")
            raise ValueError
        elif to_account not in self.accounts:
            print("Account didn't find!")
            raise ValueError
       
        self.accounts[from_account].withdraw(amount) 
        self.accounts[to_account].deposit(amount)
        print(f"Transferred {amount} from account {from_account} to account {to_account}\n")

def main():
    b = Bank()   

    user1 = BankAccount(125, 25000)  
    user2 = BankAccount(187, 15000)  

    b.add_account(user1) 
    b.add_account(user2)

    try:
        user1.deposit(10000)
        user2.withdraw(5000)
        b.transfer(125, 187, 250)
        b.transfer(125, 144, 3500) 
    except ValueError as z: 
        print(z)
    
    try:
        user1.deposit(-5000)
    except ValueError as z:
        print(z) 

    try:
        user2.withdraw(30000)
    except InsufficientFundsError as z:
        print(z)  

if __name__ == "__main__":
    main()      