class BankAccount:
    Total_Accounts = []

    def __init__(self, balance = 0, int_rate = .01):
        #default parameters for inital bank balance and interest during instiation
        self.balance = balance
        self.interest = int_rate
        BankAccount.Total_Accounts.append(self)

    def deposit(self, amount):
            #add amount to balance the account
            print(f"A deposit of ${amount} made to your account")
            self.balance += amount
            return self
    def withdraw(self, amount):
        #should subtract balance to the amount
        #should also check if sufficient balance is present prior to withdrawal
        if(self.balance < amount):
            print("Insuffient funds homie, make that cheddar first")
            return self
        else:
            print(f"A withdrawal of ${amount} has been made from your account")
            self.balance -= amount
            return self
    def display_account_info(self):
        #displays balance and interest rate
        print("Your account information is")
        print("------------------------")
        print(f"Remaining Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest *100}%")
        return self
    def yeild_interest(self):
        #applies interest to balance
        if(self.balance <= 0):
            print("You aint got no money for interest, homie")
            return self
        else:
            self.balance += (self.balance * self.interest)
            return self
    @classmethod
    def display_all_balances(cls):
        print("Account Balances for all accounts")
        print("*********************************")
        for account in cls.Total_Accounts:
            print(f"Account Balance : ${account.balance}")



user1 = BankAccount(10000, .5)
user2 = BankAccount(3000)
user1.display_account_info()
user1.deposit(5000).deposit(2500).withdraw(3000).display_account_info().yeild_interest().display_account_info()
user2.deposit(300).deposit(5000).withdraw(300).withdraw(6000).yeild_interest().display_account_info()


# user2.withdraw(300)
# user1.yeild_interest()
# user1.display_account_info()
# user2.display_account_info()

BankAccount.display_all_balances()
#displays all current bank account balances
