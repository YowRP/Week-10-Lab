from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

s = Supplier("S1", "Acme", "acme@mail.com")
p = PhysicalProduct("P1", "Laptop", 999.0, 5, 2.0, s)
d = DigitalProduct("D1", "Ebook", 10.0, 100, 5.0, s)

print("--- Before del ---")
p.display_information()
d.display_information()

del s

print("--- After del s ---")
p.display_information()
d.display_information()