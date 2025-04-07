class User:
    def __init__(self, name, id, balance, login, password):
        self.name = name
        self.id  = id
        self.balance = balance
        self.login = login
        self.password = password

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, balance: {self.balance}, login: {self.login}, password: {self.password}"    
    
    def deposit(self, bank):
        id_for_deposit = int(input("Enter Your ID - "))
        if bank.deposit_money(self,id_for_deposit):
            self.adding_money()
        else:
            print("WRONG ID!!!")

    def adding_money(self):
        money_add = float(input("How much money you want to add to your balance?\n"))
        self.balance = float(self.balance) + money_add
        return self.balance
    
    def withdraw(self, bank):
        login_for_withdraw = input("Enter Your Login - ")
        password_for_withdraw = input("Enter Your Password - ")
        if bank.withdraw_money(self, login_for_withdraw, password_for_withdraw):
            return self.withdrawing()
        else:
            print("ENTER CORRECT LOGIN AND PASSWORD!!!")

    def withdrawing(self):
        money_withdraw = float(input("How much money you want to withdraw from your balance?\n"))
        self.balance = float(self.balance) - money_withdraw
        if self.balance < 0:
            print("You don't have enough money in your balance!")
            self.balance = float(self.balance) + money_withdraw
        else:
            return self.balance    

    def check_balance(self, bank):
       id_for_checking = int(input("Enter Your ID - "))
       if bank.check(self, id_for_checking):
           return self.checking()
       else:
           print("WRONG ID!!!")

    def checking(self):
        print(f"Your balance\n{self.balance}")
         
class Bank:
    # for Singleton
    __instanse = None
 
    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)

        return cls.__instanse
    
    def __del__(self):
        Bank.__instanse = None


    def __init__(self):
        self.user = [] 

    def add_users(self, user):
        self.user.append(user)

    def show_user(self):
        for user in self.user:
            print(user)     
    
    def deposit_money(self,user,id_for_deposite):
       if user.id == id_for_deposite:
           return True
       else:
           return False
       
    def withdraw_money(self, user, login_for_withdraw, password_for_withdraw):
       if user.login == login_for_withdraw and user.password == password_for_withdraw:
           return True   
       else:
           return False
       
    def check(self, user, id_for_checking):
        if user.id == id_for_checking:
           return True       
        else:
           return False    
        
user1 = User("Artak", 4465, 10000.00, "art2003", "sdf826")
user2 = User("Hakob", 4468, 15000.00, "hak1003", "stf826")
bank = Bank() 
bank.add_users(user1)
bank.add_users(user2)
user1.deposit(bank)
user1.withdraw(bank)
user1.check_balance(bank)
bank.show_user()
# Singleton is working
bank5 = Bank()
bank5.show_user()