from __future__ import annotations
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
import os
import json

INVENTORY_FILE = "inventory.json"

class Inventory:

    def __init__ (self):
        self.__products: list[Product] = []

    def add_product (self, product: Product) -> bool :
        for i in self.__products:
            if i.get_product_id() == product.get_product_id():
                return False

        self.__products.append(product)
        return True 

    def remove_product (self, product_id: str) ->bool :
        for i in self.__products:
            if i.get_product_id() == product_id:
                self.__products.remove(i)
                return True
        else:
            return False


    def find_product (self, product_id: str) -> Product| None :
        for i in self.__products:
            if i.get_product_id() == product_id:
                return i

        return None

    def display_all(self) -> None:
        if not self.__products: #Or can add len(self.__products) == 0:
            print ("The Inventory is empty, please fill in something!")
            return 

        for i in self.__products:
            i.display_information()
            
    def get_all_as_dicts(self) -> list[dict]:
        result = []
        for i in self.__products:
            result.append(i.to_dict())
        return result

    def get_product(self) -> list[Product]:
        return self.__products
    