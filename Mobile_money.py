account_balance =100000
mobilemoneypin =12345
tax=0.5

receiver_number =int(input("Welcome to MTN mobile money.Please enter the number youre sending to :"))
amount=int(input("Enter the amount:"))
taxfee=amount*tax
reason =float(input("Enter the reason:"))
pin =int(input("Enter your mobile money pin to comfirm:"))
new_balance =account_balance-(amount+taxfee)

if amount<account_balance and mobilemoneypin==pin:
    print(f"You have successfully sent {amount} shillings to {receiver_number} at a fee of {taxfee}.Your new balance is {new_balance}.")
elif amount>account_balance and mobilemoneypin==pin:
    print(f"You have insufficient funds to complete the transaction.")  
else:
    print(f"lncorrect pin.Please try again.")  
