from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

s = Supplier("S1", "Acme", "acme@mail.com")
p = PhysicalProduct("P1", "Laptop", 999.0, 5, 2.0, s)
d = DigitalProduct("D1", "Ebook", 10.0, 100, 5.0, s)

print("--- Same function, two product types ---")
show_product_details(p)
show_product_details(d)

print("--- One inventory, one loop ---")
inventory = Inventory()
inventory.add_product(p)
inventory.add_product(d)

for product in inventory.get_product():
    show_product_details(product)