product = {
    "name": "Gigak",
    "price": 200,
    "stock": 5
}

print(product["name"])
print(product["price"]*1.2)
product["stock"] = product["stock"]-1
print(product["stock"])
product["brand"] = "logitech"
print(product["brand"])
for key, value in product.items():
    print(key,value)