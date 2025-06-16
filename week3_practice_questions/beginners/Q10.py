# 🔹 Q10: Real World Example – Product System
# Create:

# Class Product with name, price

# Class Cart that can add products and calculate total price

# Add 3 products and print the final bill.

class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Cart:
  def __init__(self):
    self.products_list = []

  def add_products(self, product):
    self.products_list.append(product)


  def total_bill(self):
    total = 0
    product_count = 0
    for product in self.products_list:
      if product.name is not None and product.price is not None:
        total += product.price
        product_count += 1

    print(f"Total Bill: Rs. {total:,}")

  
  def show_cart(self):
    print("\n🛒 Cart Items:")
    for p in self.products_list:
        print(f"- {p.name}: Rs. {p.price}")


    

    # print(f"Total Product Count: {product_count}, Total Bill: {total}")


prods1 = Product("Bike", 50000)
prods2 = Product("Car", 125000)
prods3 = Product("Bicycle", 8000)

cart = Cart()
cart.add_products(prods1)
cart.add_products(prods2)
cart.add_products(prods3)

cart.show_cart()
cart.total_bill()

