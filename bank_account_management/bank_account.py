# Bank Account Management System
# Created by Ahmet

def create_account():
    # Create a new account with username, password, and initial balance
    username = input("username :")
    password = input("password :")
    balance_input = input("enter initial balance (press enter for 0) : ")
    if balance_input == "":
        balance = 0 
    else:
        balance = float(balance_input) # Convert to float, handle potential errors later
    account = {"username": username, "password": password, "balance": balance}
    print("Account created successfully!\n")
    return account


def login_check(account):
    # Check if the provided username and password match
    inusername = input("please enter your username :")
    inpassword = input("please enter your password :")
    is_logged_in = False
    if inusername == account["username"] and inpassword == account["password"]:
        is_logged_in = True
        return is_logged_in
    else:
        return False
    

def deposit(balance, deposit_amount):
    # Deposit money into the account
    balance += float(deposit_amount)
    return balance

def withdraw(balance, amount):
    # Withdraw money from the account
    if float(amount) > balance:
        print("Insufficient balance")
    else:
       balance -= float(amount)
    return balance


choice = ""
account = create_account()
logcheck = login_check(account)

if not logcheck:
    print("Login failed. Exiting...")
    exit()
try:

    while choice != "5" and logcheck is True :

        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check your Balance")
        print("4. Account İnfo")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            a = input("Please give amount: ")
            account["balance"]= deposit(account["balance"], a)
            print("Your bank account amount is:", account["balance"])

        elif choice == "2":
            b = input("Please give amount: ")
            account["balance"] = withdraw(account["balance"], b)
            print("Your bank account amount is:", account["balance"])

        elif choice == "3":
            print("Your bank account amount is:", account["balance"])

        elif choice == "4":
            print("\nAccount info:")
            print("Username:", account["username"])
            print("Balance:", account["balance"])

        elif choice == "5":
            print("\nFinal account balance:", account["balance"])
            print("Goodbye", account["username"])

            break

        else:
            print("Invalid choice, please try again.")
except Exception as e :
    print("an error occured" , e)

