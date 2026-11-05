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

while True:
    per1 = input("Input name pls | 0 for leave")
    if per1 == "0":
        break
    print(find_product(products, per1))
