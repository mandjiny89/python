import sys
####This is Dhruv Bank Account
class BankAccount():
    owner = "Dhruv"
    balance = int()
    print(f"Bank account created for the account owner {owner} and current balance is £ {balance}")
    def __init__(self):
        print("Welcome to Dhruv's Bank Account")
    def deposit(self):
        '''Account owner can deposity money as much as he likes'''
        while True:
            user_request = input("Enter 'Y' to start the deposit, 'N' to stop: ").upper()
            if user_request == 'Y':
                deposit = int(input("Enter the Deposit ammount: "))
                BankAccount.balance = BankAccount.balance + deposit
                print(f"Money deposited to owner account and the balance is {BankAccount.balance}")
            else:
                print("Thanks for using our service, We will see you next time")
                return False

    def withdraw(self):
        '''Account owner can withdraw money but can't overdraw more than he has in the account'''
        while True:
            user_request = input("Enter 'Y' to start the withdraw, 'N' to stop: ").upper()
            if user_request == 'Y':
                withdraw = int(input("Enter the withdrawal ammount: "))
                if withdraw <= BankAccount.balance: 
                    BankAccount.balance = BankAccount.balance - withdraw
                    print(f"Money withdrawal from owner account and the current balance is {BankAccount.balance}")
                elif withdraw > BankAccount.balance:
                    print(f"Requested withdrawal is greater than current balance, please request money from availablity {BankAccount.balance}")
            else:
                print("Thanks for using our service, We will see you next time")
                return False
                sys.exit()

bank = BankAccount()
bank.deposit()
bank.withdraw()