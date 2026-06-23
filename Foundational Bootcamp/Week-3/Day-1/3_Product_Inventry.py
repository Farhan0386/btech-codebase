class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.price*self.quantity

product_list=[
    ("Laptop", 50000, 2),
    ("Mouse", 500, 10),
    ("Keyboard", 1500, 5)
]
products=[]

for name, price, quantity in product_list:
    product=Product(name, price, quantity)
    products.append(product)

grand_total = 0
print("==========Product Inventory Summary==========")
print("Product\t\tTotal Value")
print("----------------------------")
for product in products:
    value = product.total_value()
    grand_total += value
    print(f"{product.name}\t\t{value}")
print("----------------------------")
print("Grand Total Inventory Value:", grand_total)