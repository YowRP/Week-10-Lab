import json
import os
from abc import ABC, abstractmethod

INVENTORY_FILE = "inventory.json"

class Supplier:

    def __init__ (self, supplier_id: str, name: str, contact_email:str):

        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
    
    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact Email: {self.contact_email}")

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

class CanBeShipped (ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct (Product, CanBeShipped):
    def __init__ (self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier):
        super().__init__ (product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight}kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return 5.00 + (self.__weight * 2.00)

    def to_dict (self):
        data =  super().to_dict()
        data ["Type"] = "Physical"
        data ["Weight"] = self.__weight
        return data
    
class DigitalProduct (Product):
    def __init__ (self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size}MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data  = super().to_dict()
        data ["Type"] = "Digital"
        data ["Download Size"] = self.__download_size
        return data

class Inventory:

    def __init__ (self):
        self.__products = []

    def add_product (self, product):
        for i in self.__products:
            if i.get_product_id() == product.get_product_id():
                return False

        self.__products.append(product)
        return True 

    def search_product (self, product_id):
        for i in self.__products:
            if i.get_product_id() == product_id:
                return i

        return None

    def display_all(self):
        if not self.__products: #Or can add len(self.__products) == 0:
            print ("The Inventory is empty, please fill in something!")
            return 

        for i in self.__products:
            i.display_information()
            
    def get_all_as_dicts(self):
        result = []
        for i in self.__products:
            result.append(i.to_dict())
        return result

def save_inventory (inventory):
    with open (INVENTORY_FILE, "w") as f:
        json.dump(inventory.get_all_as_dicts(), f, indent = 4)

def load_inventory ():
    inventory = Inventory ()
    if os.path.exists(INVENTORY_FILE):
        print("Inventory.json Found")
        with open (INVENTORY_FILE, "r") as f:
            data = json.load(f)
            for i in data:
                if i ["Type"] == "Physical":
                    product = PhysicalProduct(i["Product ID"], i["Product Name"], i["Price"], i["Stock"], i["Weight"])

                elif i["Type"] == "Digital":
                    product = DigitalProduct(i["Product ID"], i["Product Name"], i["Price"], i["Stock"], i["Download Size"])

                else: 
                    print("Unknown Type. Skipped")
                    continue
                inventory.add_product(product)
    else:
        print("Inventory not found.")

    return inventory

#def main():
    inventory = load_inventory()

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_type = input("Product type (1. Physical, 2. Digital): ").strip()
            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue 

            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter the price of the product: ").strip())
                stock = int(input("Enter the stock amount of the product: ").strip())

                if product_type == "1":
                    weight = float(input("Enter the weight (kg): ").strip())
                    product = PhysicalProduct(product_id, name, price, stock, weight)

                elif product_type == "2":
                    download_size = float(input("Enter the download size (MB): ").strip())
                    product = DigitalProduct(product_id, name, price, stock, download_size)

            except ValueError:
                print("Invalid input, Product not added.")
                continue

            if inventory.add_product(product):
                print("Product added succesfully!")

            else:
                print("Product already exists.")

        elif choice == "3":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found")
                continue

            try:
                new_stock = int(input("Enter the new stock quantity: ").strip())

            except ValueError:
                print("Invalid value. Stock not updated.")
                continue

            if product.update_stock(new_stock):
                print("Stock updated sucessfully.")

            else:
                print("Stock cannot be negative. Stock not updated.")

        elif choice == "4":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found")
            else:
                product.display_information()


        elif choice == "5":
            save_inventory(inventory)
            print("Inventory Saved")

        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved")
            print("Thank you for your use!")
            break

        else:
            print("Invalid option.")

#if __name__ == "__main__":
    main()

if __name__ == "__main__":
    s = Supplier("S1", "Acme", "acme@mail.com")
    p = PhysicalProduct("P1", "Laptop", 999.0, 5, 2.0, s)
    d = DigitalProduct("D1", "Ebook", 10.0, 100, 5.0, s)
    p.display_information()
    d.display_information()
    del s
    p.display_information()