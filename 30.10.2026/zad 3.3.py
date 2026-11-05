products = [
    {"name" : "klava",
    "price": 150,
    "stock": 5},
    {"name" : "mouse",
    "price": 75,
    "stock": 3},
    {"name" : "kovrik",
    "price": 30,
    "stock": 9}
]

def show_products(products):
    for product in products:
        print(product)


def find_product(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product

def add_product(products, name, price, stock):
    if price >= 0 and find_product(products, name) is None:


            new_product = {"name": name,
                        "price": price,
                        "stock": stock}
            
            products.append(new_product)
            print(products)

def del_product(products, name):
    for index, product in enumerate(products):
        if product["name"].lower() == name.lower():
            del products[index]
            print(products)

def change_price(products, name, new_price):
        product = find_product(products, name)
        if new_price >= 0 and product is not None:
            
            product["price"] = new_price
            print(products)
        else:
            print("Price need to be 0 or more than 0 or there is nothing in catalogue")



        

while True:
    per1 = input("Input name pls | 0 for leave")
    
    if per1 == "0":
        break
    per2 = int(input("Input new price if needed"))
    #print(find_product(products, per1))
    add_product(products, "goika", 150, 5)
    #del_product(products, per1)
    #change_price(products, per1, per2)
