from product import Product

class OrderLine:
    def __init__ (self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        subtotal = self.__product.get_price() * self.__quantity
        return subtotal

    def display_information(self) -> None:
        print(f"Product Name: {self.__product.get_name()}, Quantity: {self.__quantity}, Subtotal: {self.calculate_subtotal():.2f}")

    def get_product(self) -> Product:
        return self.__product
    


