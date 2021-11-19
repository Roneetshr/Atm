pin = 12345 
pinenter = input("Enter Pin: ")
Welcome = "Welcome Roneet to the ATM"
Choice = input("Type 1 to Withdraw/Type 2 to Deposite: ")
Money = 0




if pinenter == 12345:
    print(Welcome)
    print(Choice)

if Choice == 1:
    print("you have" +"$"+ Money)
    Withdraw = input("Enter Withdrawal: ")
    if Withdraw > Money:
        print("Sorry cannot complete transaction")
    if Withdraw < Money:
        print("Added $" + Withdraw + "To wallet/card")
        Money = Money + Withdraw
        Choice = input("Type 1 to Withdraw/Type 2 to Deposite: ")

if Choice == 2:
      print("you have" +"$"+ Money)
      Deposite = input("Enter Deposite: ")
      Money = Money + Withdraw
      print("Added $" + Withdraw + "To atm")
      Choice = input("Type 1 to Withdraw/Type 2 to Deposite: ") 

 

    

