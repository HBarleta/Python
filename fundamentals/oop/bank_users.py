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
        if(self.balance < amount):
            print("Insuffient funds homie, make that cheddar first")
            return self
        else:
            if validated_acct == "savings":
                print(f"A withdrawal of ${amount} has been made from your {validated_acct} account")
                print("------------------------")
                self.savingsacct -= amount
            elif validated_acct == "checking":
                print(f"A withdrawal of ${amount} has been made from your {validated_acct} account")
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
        #checks if there is any money to give interest to
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
        print("************************")
        for account in cls.Total_Accounts:
            print(f"Checking Account Balance : ${account.balance}")
            print(f"Savings Account Balance : ${account.savingsacct}")
            print("------------------------")

class BankUsers:
    UserList = {} #adds user data to dictionary that will link bank accounts to user names
    def __init__(self, name, email, savings_deposit=0, savings_interest=0.1, deposit=0, interest=.01):
        self.userName = name
        self.email = email
        self.accounts = BankAccount(savings_deposit, savings_interest, deposit, interest)
        BankUsers.UserList[name] = self

    def userBalance(self):
        print("************************")
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
    @classmethod #ALL CLASS METHODS MUST BE UNDER THIS DECORATOR
    #transfer money from savings between accounts
    #account names must match when passing arguments
    def transfer_money_savings(cls, from_savings, to_savings, amount):
        transfer_from = cls.UserList[from_savings].accounts
        transfer_to = cls.UserList[to_savings].accounts
        if (transfer_from.savingsacct - amount) < 0:
                print("***********************")
                print("Not enough resources!")
                print("***********************")
        else:
            transfer_from.savingsacct -= amount
            transfer_to.savingsacct += amount
            print("<^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^><^><^><^")
            print("<^>                                                                       <^>")
            print(f"<^> A savings account transfer of ${amount} has been made from {from_savings} to {to_savings}  <^>")
            print("<^>                                                                       <^>")
            print("<^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^><^><^><^")
    @classmethod #ALL CLASS METHODS MUST BE UNDER THIS DECORATOR
    #transfer money from checking between accounts
    #account names must match when passing arguments
    def transfer_money_checking(cls, from_acct, to_account, amount):
            transfer_from = cls.UserList[from_acct].accounts
            transfer_to = cls.UserList[to_account].accounts
            if (transfer_from.balance - amount) < 0:
                print("*********************")
                print("Not enough resources!")
                print("*********************")
            else:
                transfer_from.balance -= amount
                transfer_to.balance += amount
                print("<^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^>")
                print("<^>                                                                        <^>")
                print(f"<^> A checking account transfer of ${amount} has been made from {from_acct} to {to_account}  <^>")
                print("<^>                                                                        <^>")
                print("<^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^><^>^<><^><^>")
    
user_Harold = BankUsers("Harold", "Hbf20c@gmail.com", 500, .07, 5000, .03)
user_Jash = BankUsers("Jash", "Mustang5.0@aol.com", 300, .02, 3000, 0.05 )
user_Harold.userBalance()
user_Jash.userBalance()
user_Harold.userWithdraw("checking", 300)
user_Harold.userDeposit("checking", 2)
user_Jash.userYieldInt()
BankUsers.transfer_money_checking("Jash", "Harold", 500)
user_Harold.userBalance()
user_Jash.userBalance()
BankUsers.transfer_money_savings("Harold", "Jash", 300)
BankUsers.transfer_money_savings("Harold", "Jash", 100)
user_Harold.userBalance()
user_Jash.userBalance()
