import time  

print("Please Enter your CARD")
time.sleep(2)  

password = 1234
balance = 5000
transaction_history = []  

pin = int(input("Enter your ATM PIN: "))

if pin == password:
    while True:
        print("""
        1 == Check Balance
        2 == Withdraw Cash
        3 == Deposit Cash
        4 == Change PIN
        5 == View Transaction History
        6 == Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue 

        # Option 1: Account balance inquiry
        if option == 1:
            print(f"Your current balance is ₹{balance}")
            transaction_history.append(f"Checked balance: ₹{balance}")
            print("=============================================")

        # Option 2: Cash withdrawal
        elif option == 2:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient balance!")
            else:
                balance -= withdraw_amount 
                print(f"₹{withdraw_amount} is debited from your account")
                transaction_history.append(f"Withdrew: ₹{withdraw_amount}")
                print(f"Your updated balance is ₹{balance}")
            print("=============================================")

        # Option 3: Cash deposit
        elif option == 3:
            deposit_amount = int(input("Enter amount to deposit: "))
            balance += deposit_amount  
            print(f"₹{deposit_amount} is credited to your account")
            transaction_history.append(f"Deposited: ₹{deposit_amount}")
            print(f"Your updated balance is ₹{balance}")
            print("=============================================")

        # Option 4: PIN change
        elif option == 4:
            new_pin = int(input("Enter your new PIN: "))
            password = new_pin 
            print("Your PIN has been successfully changed!")
            transaction_history.append("Changed PIN")
            print("=============================================")

        # Option 5: Transaction history
        elif option == 5:
            print("Transaction History:")
            if not transaction_history:
                print("No transactions found.")
            else:
                for transaction in transaction_history:
                    print(transaction)
            print("=============================================")

        # Option 6: Exit
        elif option == 6:
            print("Exiting... Thank you for using the ATM.")
            break  

        else:
            print("Invalid option! Please try again.")
            print("=============================================")

else:
    print("Invalid PIN. Please try again.")



        







