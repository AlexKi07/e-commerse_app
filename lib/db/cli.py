# lib/db/cli.py
from database import SessionLocal
import crud
import models

def main():
    db = SessionLocal()

    def print_menu():
        print("\nE-commerce CLI")
        print("1. List Customers")
        print("2. Add Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. List Categories")
        print("6. Add Category")
        print("7. List Products")
        print("8. Add Product")
        print("9. Place Order")
        print("10. List Orders")
        print("0. Exit")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            customers = crud.get_all_customers(db)
            for c in customers:
                print(f"{c.id}: {c.name} ({c.email})")

        elif choice == "2":
            name = input("Customer name: ")
            email = input("Customer email: ")
            customer = crud.create_customer(db, name, email)
            print(f"Created customer ID {customer.id}")

        elif choice == "3":
            customer_id = int(input("Customer ID to update: "))
            name = input("New name: ")
            email = input("New email: ")
            updated = crud.update_customer(db, customer_id, name, email)
            if updated:
                print("Customer updated.")
            else:
                print("Customer not found.")

        elif choice == "4":
            customer_id = int(input("Customer ID to delete: "))
            deleted = crud.delete_customer(db, customer_id)
            if deleted:
                print("Customer deleted.")
            else:
                print("Customer not found.")

        elif choice == "5":
            categories = crud.get_all_categories(db)
            for cat in categories:
                print(f"{cat.id}: {cat.name}")

        elif choice == "6":
            name = input("Category name: ")
            category = crud.create_category(db, name)
            print(f"Created category ID {category.id}")

        elif choice == "7":
            products = crud.get_all_products(db)
            for p in products:
                print(f"{p.id}: {p.name} - ${p.price} (Category ID: {p.category_id})")

        elif choice == "8":
            name = input("Product name: ")
            price = float(input("Product price: "))
            category_id = int(input("Category ID: "))
            product = crud.create_product(db, name, price, category_id)
            print(f"Created product ID {product.id}")

        elif choice == "9":
            customer_id = int(input("Customer ID: "))
            items = []
            print("Enter product IDs and quantities (empty product ID to finish):")
            while True:
                prod_id = input("Product ID: ").strip()
                if not prod_id:
                    break
                quantity = int(input("Quantity: "))
                items.append({"product_id": int(prod_id), "quantity": quantity})
            order = crud.create_order(db, customer_id, items)
            print(f"Order {order.id} placed.")

        elif choice == "10":
            orders = crud.get_all_orders(db)
            for order in orders:
                print(f"Order {order.id} by Customer {order.customer_id} on {order.order_date}")
                for item in order.order_items:
                    print(f"  Product {item.product_id}, Qty: {item.quantity}")

        elif choice == "0":
            print("Exiting CLI.")
            break

        else:
            print("Invalid choice. Try again.")

    db.close()

if __name__ == "__main__":
    main()
