products = {"mouse": 80.00,
            "klava": 200.00}


while True:
    try:
        user_money = float(input("Сколько у тя денег: "))
        if user_money >= 0.00:
            break
        else:
            print("Your balance cannot be negative.")


    except ValueError:
        print("Please write down the money, not words")




while True:

    name_product = input("Название Товара: (0 что бы выйти)")

    if name_product == "0":
            break

    for name, price in products.items():
        if name_product.lower() == name:
            print("I have found your product!")
            if user_money >= price:
                user_money -= price
                print(f"Sucess, your balance is {user_money:.2f}")
            
                if user_money == 0:
                    print("Your balance is Zero, please, donate something lol")
                    
                break
            else:
                print(f"You don`t have money for that. You need {price-user_money:.2f}")
                break
    else:
        print("We didn`t found your product")

    

