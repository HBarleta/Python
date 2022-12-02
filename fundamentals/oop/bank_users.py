class BankAccount:
    Total_Accounts = []

    def __init__(self, savings=0, savings_int_rate=0, balance = 0, int_rate = .01):
        #default parameters for inital bank balance and interest during instiation
        self.balance = balance
        self.interest = int_rate
        self.savingsacct = savings
        self.savingsint = savings_int_rate
        BankAccount.Total_Accounts.append(self)

    def deposit(self, which_acct, amount):
        validated_acct = which_acct.lower()
        #add amount to balance the account 
        if(validated_acct == "savings"):
            print(f"A deposit of ${amount} made to your {validated_acct} account")
            print("------------------------")
            self.savingsacct += amount
        elif(validated_acct == "checking"):
            print(f"A deposit of ${amount} made to your {validated_acct} account")
            print("------------------------")
            self.balance += amount
        else:
            print("Please specify 'checking' or 'savings' accounts")
        return self
    def withdraw(self, which_acct, amount):
        #should subtract balance to the amount
        #should also check if sufficient balance is present prior to withdrawal
        validated_acct = which_acct.lower()
        print(which_acct)
        if(self.balance < amount):
            print("Insuffient funds homie, make that cheddar first")
            return self
        else:
            if(validated_acct == "savings"):
                print(f"A withdrawal of ${amount} has been made from your {validated_acct} account")
                print("------------------------")
                self.savingsacct -= amount
            elif(validated_acct == "checking"):
                print(f"A withdrawal of ${amount} has been made from your {validated_acct}account")
                print("------------------------")
                self.balance -= amount
            else:
                print("Please specify 'checking' or 'savings' accounts")
            return self
    def display_account_info(self):
        #displays balance and interest rate
        print("------------------------")
        print("Your account information")
        print("------------------------")
        print("------------------------")
        print("Checking Account Balance")
        print("------------------------")
        print(f"Remaining Balance: ${self.balance}")
        print(f"Interest Rate: {round((self.interest * 100), 2)}%")
        print("------------------------")
        print("Savings Account Balance")
        print("------------------------")
        print(f"Remaining Balance: ${self.savingsacct}")
        print(f"Savings Interest Rate: {round((self.savingsint *100), 2)}%")
        print("------------------------")
        return self
    def yeild_interest(self):
        #applies interest to balance
        interest_yield_amount = round((self.balance * self.interest), 3)
        if(self.balance <= 0):
            print("You aint got no money for interest, homie")
            return self
        else:
            self.balance += (self.balance * self.interest)
            print("------------------------")
            print(f"An interest payment of ${interest_yield_amount} has been added to your account")
            print("------------------------")
            return self
    @classmethod
    def display_all_balances(cls):
        print("Account Balances for all accounts")
        print("*********************************")
        for account in cls.Total_Accounts:
            print(f"Account Balance : ${account.balance}")
            print("------------------------")

class BankUsers:
    UserList = {}
    def __init__(self, name, email, savings_deposit=0, savings_interest=0.1, deposit=0, interest=.01):
        self.userName = name
        self.email = email
        self.accounts = BankAccount(savings_deposit, savings_interest, deposit, interest)
        BankUsers.UserList[name] = self

    def userBalance(self):
        print("*********************************")
        print(f"      {self.userName}      ")
        self.accounts.display_account_info()

    def userDeposit(self, which_acct, deposit_amount):
        self.accounts.deposit(which_acct, deposit_amount)
        return self

    def userWithdraw(self, which_acct, withdraw_amount):
        self.accounts.withdraw(which_acct, withdraw_amount)
        return self
    
    def userYieldInt(self):
        self.accounts.yeild_interest()
    @classmethod
    def transfer_money_checking(cls, from_acct, to_account, amount):
        transfer_from = cls.UserList[from_acct].accounts
        transfer_to = cls.UserList[to_account].accounts
        transfer_from.balance -= amount
        transfer_to.balance += amount
        print("////////////////////////////////////////////////////////")
        print(f"//A transfer of ${amount} has been made from {from_acct} to {to_account}//")
        print("////////////////////////////////////////////////////////")


user_Harold = BankUsers("Harold", "Hbf20c@gmail.com", 500, .07, 5000, .03)
user_Jash = BankUsers("Jash", "Mustang5.0@aol.com", 300, .02, 0, 0.05 )
user_Harold.userBalance()
user_Jash.userBalance()
BankUsers.transfer_money_checking("Harold", "Jash", 500)
user_Harold.userBalance()
user_Jash.userBalance()