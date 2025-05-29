from lib.db import crud
from lib.db.database import SessionLocal, init_db

def show_menu():
    print("\n--- E-commerce Management CLI ---")
    print("1. Register a new customer account")
    print("2. View all customers")
    print("3. View customer by ID")
    print("4. Update customer information")
    print("5. Delete customer account")
    print("\n--- Category ---")
    print("6. Create a new category")
    print("7. List all categories")
    print("8. Fetch a category by ID")
    print("9. Update a category")
    print("10. Delete a category")
    print("\n--- Products ---")
    print("11. Add a new product")
    print("12. View all products")
    print("13. View product by ID")
    print("14. Edit a product")
    print("15. Delete a product")
    print("\n--- Orders ---")
    print("16. Place a new order")
    print("17. View all orders")
    print("18. View order by ID")
    print("19. Edit an order")
    print("20. Cancel/delete an order")
    print("\n--- Exit ---")
    print("0. Exit")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    init_db()
    db = SessionLocal()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        # The Customers 
        elif choice == "1":
            name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()
            customer = crud.create_customer(db, name, email)
            print(f"Customer created with ID: {customer.id}")

        elif choice == "2":
            customers = crud.get_all_customers(db)
            if customers:
                print("\nCustomers:")
                for c in customers:
                    print(f"ID: {c.id}, Name: {c.name}, Email: {c.email}")
            else:
                print("No customers found.")

        elif choice == "3":
            cust_id = input_int("Enter customer ID: ")
            customer = crud.get_customer_by_id(db, cust_id)
            if customer:
                print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
            else:
                print("Customer not found.")

        elif choice == "4":
            cust_id = input_int("Enter customer ID to update: ")
            name = input("Enter new name: ").strip()
            email = input("Enter new email: ").strip()
            customer = crud.update_customer(db, cust_id, name, email)
            if customer:
                print("Customer updated successfully.")
            else:
                print("Customer not found.")

        elif choice == "5":
            cust_id = input_int("Enter customer ID to delete: ")
            customer = crud.delete_customer(db, cust_id)
            if customer:
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")

        # The Categories 
        elif choice == "6":
            name = input("Enter category name: ").strip()
            category = crud.create_category(db, name)
            print(f"Category created with ID: {category.id}")

        elif choice == "7":
            categories = crud.get_all_categories(db)
            if categories:
                print("\nCategories:")
                for cat in categories:
                    print(f"ID: {cat.id}, Name: {cat.name}")
            else:
                print("No categories found.")

        elif choice == "8":
            cat_id = input_int("Enter category ID: ")
            category = crud.get_category_by_id(db, cat_id)
            if category:
                print(f"ID: {category.id}, Name: {category.name}")
            else:
                print("Category not found.")

        elif choice == "9":
            cat_id = input_int("Enter category ID to update: ")
            name = input("Enter new category name: ").strip()
            category = crud.update_category(db, cat_id, name)
            if category:
                print("Category updated successfully.")
            else:
                print("Category not found.")

        elif choice == "10":
            cat_id = input_int("Enter category ID to delete: ")
            category = crud.delete_category(db, cat_id)
            if category:
                print("Category deleted successfully.")
            else:
                print("Category not found.")

        # The Products 
        elif choice == "11":
            name = input("Enter product name: ").strip()
            price_str = input("Enter product price: ").strip()
            try:
                price = float(price_str)
            except ValueError:
                print("Invalid price.")
                continue
            cat_id = input_int("Enter category ID: ")
            category = crud.get_category_by_id(db, cat_id)
            if not category:
                print("Category not found. Cannot create product.")
                continue
            product = crud.create_product(db, name, price, cat_id)
            print(f"Product created with ID: {product.id}")

        elif choice == "12":
            products = crud.get_all_products(db)
            if products:
                print("\nProducts:")
                for p in products:
                    print(f"ID: {p.id}, Name: {p.name}, Price: ${p.price:.2f}, Category ID: {p.category_id}")
            else:
                print("No products found.")

        elif choice == "13":
            prod_id = input_int("Enter product ID: ")
            product = crud.get_product_by_id(db, prod_id)
            if product:
                print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}, Category ID: {product.category_id}")
            else:
                print("Product not found.")

        elif choice == "14":
            prod_id = input_int("Enter product ID to update: ")
            product = crud.get_product_by_id(db, prod_id)
            if not product:
                print("Product not found.")
                continue
            name = input(f"Enter new name (current: {product.name}): ").strip()
            price_str = input(f"Enter new price (current: {product.price}): ").strip()
            try:
                price = float(price_str)
            except ValueError:
                print("Invalid price.")
                continue
            cat_id = input_int(f"Enter new category ID (current: {product.category_id}): ")
            category = crud.get_category_by_id(db, cat_id)
            if not category:
                print("Category not found.")
                continue
            updated = crud.update_product(db, prod_id, name, price, cat_id)
            print("Product updated successfully.")

        elif choice == "15":
            prod_id = input_int("Enter product ID to delete: ")
            product = crud.delete_product(db, prod_id)
            if product:
                print("Product deleted successfully.")
            else:
                print("Product not found.")

        #  Orders 
        elif choice == "16":
            cust_id = input_int("Enter customer ID placing the order: ")
            customer = crud.get_customer_by_id(db, cust_id)
            if not customer:
                print("Customer not found.")
                continue

            items = []
            print("Add products to the order. Enter 'done' when finished.")
            while True:
                prod_input = input("Product ID (or 'done'): ").strip()
                if prod_input.lower() == 'done':
                    break
                try:
                    prod_id = int(prod_input)
                except ValueError:
                    print("Invalid product ID.")
                    continue
                product = crud.get_product_by_id(db, prod_id)
                if not product:
                    print("Product not found.")
                    continue
                qty = input_int("Quantity: ")
                if qty <= 0:
                    print("Quantity must be positive.")
                    continue
                items.append({"product_id": prod_id, "quantity": qty})
            if not items:
                print("No items added. Order not created.")
                continue
            order = crud.create_order(db, cust_id, items)
            print(f"Order created with ID: {order.id}")

        elif choice == "17":
            orders = crud.get_all_orders(db)
            if orders:
                print("\nOrders:")
                for o in orders:
                    print(f"ID: {o.id}, Customer ID: {o.customer_id}, Date: {o.order_date}")
            else:
                print("No orders found.")

        elif choice == "18":
            order_id = input_int("Enter order ID: ")
            order = crud.get_order_by_id(db, order_id)
            if order:
                print(f"Order ID: {order.id}, Customer ID: {order.customer_id}, Date: {order.order_date}")
                print("Items:")
                for item in order.order_items:
                    print(f"  Product ID: {item.product_id}, Quantity: {item.quantity}")
            else:
                print("Order not found.")

        elif choice == "19":
            order_id = input_int("Enter order ID to update: ")
            order = crud.get_order_by_id(db, order_id)
            if not order:
                print("Order not found.")
                continue

            items = []
            print("Enter new products and quantities for this order. Enter 'done' when finished.")
            while True:
                prod_input = input("Product ID (or 'done'): ").strip()
                if prod_input.lower() == 'done':
                    break
                try:
                    prod_id = int(prod_input)
                except ValueError:
                    print("Invalid product ID.")
                    continue
                product = crud.get_product_by_id(db, prod_id)
                if not product:
                    print("Product not found.")
                    continue
                qty = input_int("Quantity: ")
                if qty <= 0:
                    print("Quantity must be positive.")
                    continue
                items.append({"product_id": prod_id, "quantity": qty})
            if not items:
                print("No items provided. Order not updated.")
                continue
            crud.update_order_items(db, order_id, items)
            print("Order updated successfully.")

        elif choice == "20":
            order_id = input_int("Enter order ID to delete: ")
            order = crud.delete_order(db, order_id)
            if order:
                print("Order deleted successfully.")
            else:
                print("Order not found.")

        else:
            print("Invalid choice. Please try again.")

    db.close()

if __name__ == "__main__":
    main()
