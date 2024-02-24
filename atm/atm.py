def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 1000:
        balance += amount
        print("Cash deposited. Current balance:", balance)
    else:
        print("Deposit amount must be greater than 1000.")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > 1000:
        if balance >= amount:
            balance -= amount
            print("Cash withdrawn. Current balance:", balance)
        else:
            print("Insufficient funds.")
    else:
        print("Withdrawal amount must be greater than 1000.")
    return balance

def check_balance(balance):
    print("Your balance is:", balance)

def atm():
    balance = 0

    while True:
        print("\nATM Menu:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Thank you for using the ATM. Goodbye!")
            break
        elif choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            check_balance(balance)
        else:
            print("Invalid input. Please try again.")

atm()