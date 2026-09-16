def total(**items):
    return sum(items.values())

item_values = {
    "apple": 2.50,
    "bread": 3.00,
    "milk": 1.50
}

print(f"${total(**item_values)}")