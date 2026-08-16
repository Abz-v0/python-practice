products = []

while True:
    name = input("Product Name: ")
    if name == "done": break
    price = float(input("Price: "))
    product = {"Product name": name, "Price": price}
    products.append(product)

for i in range(len(products)):
    print(i + 1,products[i]['Product name'], f"₦{products[i]['Price']:,.2f}")