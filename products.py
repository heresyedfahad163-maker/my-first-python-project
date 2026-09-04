products=[
    {"name": "Laptop", "price": 1200, "stock":6},
    {"name": "Phone", "price": 800, "stock":8},
    {"name": "Tablet", "price": 5000, "stock":9},
    {"name": "PC", "price": 1500, "stock":4},
]

total_value=0

print("Inventory Report")
print("-" * 40)

for product in products:
    value = product["price"] * product["stock"]
    total_value += value

    print(
        f"{product['name']:<10}=> ${value:>5}"
    )

    print("-" * 40)
    print("\nTotal Inventory Value:")
    print(total_value)