user_details = {"Name" : "Tarun kakara",
                "mobile no": 123443345,
                "ATM PIN" : "4495",
                "Balance" : 12304,
                "Transaction history" : []
}

print("Please Insert you ATM CARD")

attempts = 3


while attempts > 0 :
    user_pin = input("Enter your pin: ")

    if len(user_pin) == 4 :
        if user_pin in user_details["ATM PIN"] :
             print("Welcome to ATM")
             break
        else:
                if attempts > 1:
                    attempts -= 1
                    print(f"{user_pin} is incorrect please try again you have {attempts} attempts left")
                else:
                    print("Card is Blocked!!!")
                    break
    else:
         print("Wrong pin try again!!!")
         exit
