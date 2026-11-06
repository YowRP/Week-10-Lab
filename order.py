from order_line import OrderLine
from product import Product

class Order:
    def __init__ (self, order_id: str) -> None :
        self.__order_id = order_id
        self.__orderlines: list[OrderLine] =[]

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__orderlines.append(order_line)

    def calculate_total (self) -> float:
        total = 0.0
        for i in self.__orderlines:
            total += i.calculate_subtotal()
        return total

    def remove_order_line(self, product_id: str) -> bool:
        for i in self.__orderlines:
            identification = i.get_product().get_product_id()
            if product_id == identification:
                self.__orderlines.remove(i)
                return True
        
        return False
            
    def get_order_lines(self) -> list[OrderLine]:
        return self.__orderlines

    def display_information(self) -> None:
        print(f"Order ID: {self.__order_id}")
        for i in self.__orderlines:
            i.display_information()

        print(f"Total: {self.calculate_total()}")
