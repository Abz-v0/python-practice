def main():
    # get user info
    item = input("Item: ").strip().title()
    price = float(input("Price per unit: "))
    quantity = float(input("Quantity: "))

    total = calculate_total(price, quantity)

    # show the receipt        
    print(f"Item: {item} | Total: {total:,.2f}")

def calculate_total(price, quantity):
    return  price * quantity
        

main()