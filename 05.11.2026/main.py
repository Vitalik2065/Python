


def get_valid_price():
    while True:

        try:
            price = int(input("Write down please price for product: "))
            if price >= 0:
                return price
            else:
                print("Negative number")
                

            
        except ValueError:
            print("It has to be number brooo")
        



per2 = get_valid_price()
print(per2)
