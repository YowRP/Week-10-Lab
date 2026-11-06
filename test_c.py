from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

s = Supplier("S1", "Nike", "Nike@gmail.com")
p = PhysicalProduct("P001", "Hammer", 40, 3, 4.7, s)
d = DigitalProduct("D001", "Sloare", 30, 2, 5.8, s)

#Order 1
print("------ Order 1 --------")
Order_1 = Order("ORD01")
Order_1.add_order_line(p,2)
Order_1.add_order_line(d,4)

Order_1.display_information()

#Order 2 
print("--------Order 2 -------")
Order_2 = Order("ORD02")
Order_2.add_order_line(p,3)
Order_2.add_order_line(d,8)

Order_2.display_information()

print("------ Proof ------")
line_1 = Order_1.get_order_lines()[0]    # Hammer line in Order 1
line_2 = Order_2.get_order_lines()[0]    # Hammer line in Order 2
print("Same Product object?", line_1.get_product() is line_2.get_product())

if line_1 is line_2:
    print("Both are the same!")

else:
    print("Both are different")

print(id(line_1.get_product()))
print(id(line_2.get_product()))

Order_1.remove_order_line("D001") #expect True
Order_1.display_information() #total should be $80
Order_1.remove_order_line("X999") #expect False
