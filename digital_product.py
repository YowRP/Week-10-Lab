from product import Product
from supplier import Supplier

class DigitalProduct (Product):
    def __init__ (self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self.__download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        data  = super().to_dict()
        data ["Type"] = "Digital"
        data ["Download Size"] = self.__download_size
        return data