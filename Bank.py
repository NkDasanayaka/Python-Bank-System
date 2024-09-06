class bank_account:
    # open bank account with account number and initial balance
    def __init__(self, account_number, initial_deposit):
        self.acc_number = account_number
        self.balance = initial_deposit
        print("Your bank account is created successfully.Your account number is: ", account_number)
        print("Your account balance is : Rs.", initial_deposit)

        # deposit money into the account

    def deposit(self, amount):
        # check if the deposit amount is positive
        if amount > 0:
            # return true when deposit done successfully
            self.balance += amount
            return True
            # return false when the deposit is failed
        else:
            print("please deposit positive value")
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful. Your remaining balance is: Rs.{self.balance:.2f}")
            else:
                # withdrawal fails because of insufficient balance in the account
                print("insufficient balance.")
        else:
            print("Your withdrawal amount must be positive.")


# main function to operate bank accounts system.
def main():
    accounts = {}
    while True:
        print("\n1.Create Account")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Check Balance")
        print("5.Transfer money")
        print("6.Exit")

        # get choice from customer
        choice = input("Enter Your choice: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            transfer(accounts)
        elif choice == '6':
            print("Thank You")
            break
        else:
            print("Please enter a valid choice")


# Open new account
def create_account(accounts):
    # check if the account is already exists
    account_number = input("Enter Your account number:")
    if account_number in accounts:
        print("You already have an account")
        return
    initial_deposit = int(input("Enter initial deposit amount: "))
    # check the initial deposit is positive
    if initial_deposit <= 0:
        print("Initial amount should be positive value.")
        return
    accounts[account_number] = bank_account(account_number, initial_deposit)
    print("Your account is created successfully")


# Deposit money into an existing account
def deposit(accounts):
    # input account number
    account_number = input("Enter your account number: ")
    # check whether the account already exists or not
    if account_number in accounts:
        amount = int(input("Enter your deposit amount: "))
        # check the deposit amount is positive
        if amount > 0:
            accounts[account_number].deposit(amount)
            print("Deposit successful. Your account balance is: ", accounts[account_number].balance)
        else:
            print("Deposit amount should be positive value.")
    else:
        print("Check your account number(account not found)")


# operation to check account balance of an account.
def check_balance(accounts):
    # Enter the account number
    account_number = input("Enter your account number: ")
    #check if the account is valid
    if account_number in accounts:
        print("Your account balance: ", accounts[account_number].balance)

    else:
        print("Account not found.")

# operation to withdraw from an account.
def withdraw(accounts):
    account_number = input("Enter your account number: ")
    #chech if the account number is valid.
    if account_number not in accounts:
        print("Account not found. Please check your account number again.")
        return
    #enter amount
    amount = float(input("Enter amount to withdraw: "))
    #check whether the amount is positive.
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return
    accounts[account_number].withdraw(amount)


# operation to transfer money among accounts.
def transfer(accounts):
    account_1 = input("Enter your account number : ")
    #check  if the sender's account is valid
    if account_1 not in accounts:
        print("Your account not found. Please check your account number again.")
        return
    #check if the receiver's account is valid
    account_2 = input("Enter receiver's account number: ")
    if account_2 not in accounts:
        print("Receiver's account not found. Please check the account number again.")
        return
    #enter transferring amount
    amount = float(input("Enter transfer amount: "))
    if amount <= 0:
        print("Transfer amount must be positive.")
        return

    if accounts[account_1].withdraw(amount):
        accounts[account_2].deposit(amount)
        print(f"Transfer successful. Your new balance is: Rs.{accounts[account_1].balance:.2f}")
    else:
        print("Insufficient balance for transfer.")

if __name__ == "__main__":
    main()
