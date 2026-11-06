from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
import os 
import json

INVENTORY_FILE = "inventory.json"

def save_inventory (inventory: Inventory) -> None :
    with open (INVENTORY_FILE, "w") as f:
        json.dump(inventory.get_all_as_dicts(), f, indent = 4)

def load_inventory () -> Inventory :
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

def main() -> None:
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
            product = inventory.find_product(product_id)
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
            product = inventory.find_product(product_id)
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

if __name__ == "__main__":
    main()
