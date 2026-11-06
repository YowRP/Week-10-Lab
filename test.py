from Inventory_manager import Supplier, PhysicalProduct, Inventory

s = Supplier("S1", "Acme", "acme@mail.com")
p = PhysicalProduct("P1", "Laptop", 999.0, 5, 2.0, s)   # created before any inventory

inv_a = Inventory()
inv_b = Inventory()

print("--- add to A ---")
print(inv_a.add_product(p))

print("--- remove from A ---")
print(inv_a.remove_product("P1"))
print("Found in A?", inv_a.find_product("P1"))

print("--- product still works? ---")
p.display_information()

print("--- add to B ---")
print(inv_b.add_product(p))
print("Same object?", inv_b.find_product("P1") is p)