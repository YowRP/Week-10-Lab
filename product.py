from abc import ABC, abstractmethod
from supplier import Supplier

class Product (ABC):

    def __init__ (self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock  = stock
        self.__supplier = supplier

    def update_stock(self, quantity: int)-> bool :

        if quantity < 0 :
            return False

        else:
            self.__stock = quantity
            return True

    def display_information (self) -> None:
        print (f"Product ID:  {self.__product_id} | Product Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")
        self.__supplier.display_information()

    def get_product_id (self)-> str:
         get_product_ID = self.__product_id
         return get_product_ID

    def to_dict(self) -> dict:
        return {"Product ID": self.__product_id, "Product Name": self.__name, "Price": self.__price, "Stock": self.__stock}

    @abstractmethod
    def get_fulfilment_info (self) -> str:
        pass