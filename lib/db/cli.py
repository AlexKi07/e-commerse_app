
# from database import SessionLocal
# import crud
# import models

# def main():
#     db = SessionLocal()

#     def print_menu():
#         print("\n--- E-commerce CLI ---")
#         print("CUSTOMERS")
#         print("1. Register New Customer")
#         print("2. List All Customers")
#         print("3. View Customer by ID")
#         print("4. Update Customer Info")
#         print("5. Delete Customer")

#         print("\nCATEGORIES")
#         print("6. Create Category")
#         print("7. List All Categories")
#         print("8. View Category by ID")
#         print("9. Update Category")
#         print("10. Delete Category")

#         print("\nPRODUCTS")
#         print("11. Add Product")
#         print("12. List All Products")
#         print("13. View Product by ID")
#         print("14. Update Product")
#         print("15. Delete Product")

#         print("\nORDERS")
#         print("16. Place New Order")
#         print("17. List All Orders")
#         print("18. View Order by ID")
#         print("19. Edit Order (Change quantities)")
#         print("20. Cancel/Delete Order")

#         print("\n0. Exit")

#     while True:
#         print_menu()
#         choice = input("Select an option: ").strip()

#         # --- Customers ---
#         if choice == "1":
#             name = input("Customer name: ")
#             email = input("Customer email: ")
#             customer = crud.create_customer(db, name, email)
#             print(f"Customer created with ID {customer.id}")

#         elif choice == "2":
#             customers = crud.get_all_customers(db)
#             for c in customers:
#                 print(f"{c.id}: {c.name} ({c.email})")

#         elif choice == "3":
#             customer_id = int(input("Customer ID: "))
#             customer = crud.get_customer_by_id(db, customer_id)
#             if customer:
#                 print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
#             else:
#                 print("Customer not found.")

#         elif choice == "4":
#             customer_id = int(input("Customer ID to update: "))
#             name = input("New name: ")
#             email = input("New email: ")
#             updated = crud.update_customer(db, customer_id, name, email)
#             print("Customer updated." if updated else "Customer not found.")

#         elif choice == "5":
#             customer_id = int(input("Customer ID to delete: "))
#             deleted = crud.delete_customer(db, customer_id)
#             print("Customer deleted." if deleted else "Customer not found.")

#         # --- Categories ---
#         elif choice == "6":
#             name = input("Category name: ")
#             category = crud.create_category(db, name)
#             print(f"Category created with ID {category.id}")

#         elif choice == "7":
#             categories = crud.get_all_categories(db)
#             for cat in categories:
#                 print(f"{cat.id}: {cat.name}")

#         elif choice == "8":
#             category_id = int(input("Category ID: "))
#             category = crud.get_category_by_id(db, category_id)
#             if category:
#                 print(f"ID: {category.id}, Name: {category.name}")
#             else:
#                 print("Category not found.")

#         elif choice == "9":
#             category_id = int(input("Category ID to update: "))
#             name = input("New category name: ")
#             updated = crud.update_category(db, category_id, name)
#             print("Category updated." if updated else "Category not found.")

#         elif choice == "10":
#             category_id = int(input("Category ID to delete: "))
#             deleted = crud.delete_category(db, category_id)
#             print("Category deleted." if deleted else "Category not found.")

#         # --- Products ---
#         elif choice == "11":
#             name = input("Product name: ")
#             price = float(input("Product price: "))
#             category_id = int(input("Category ID: "))
#             product = crud.create_product(db, name, price, category_id)
#             print(f"Product created with ID {product.id}")

#         elif choice == "12":
#             products = crud.get_all_products(db)
#             for p in products:
#                 print(f"{p.id}: {p.name} - ${p.price} (Category ID: {p.category_id})")

#         elif choice == "13":
#             product_id = int(input("Product ID: "))
#             product = crud.get_product_by_id(db, product_id)
#             if product:
#                 print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category ID: {product.category_id}")
#             else:
#                 print("Product not found.")

#         elif choice == "14":
#             product_id = int(input("Product ID to update: "))
#             name = input("New product name: ")
#             price = float(input("New price: "))
#             category_id = int(input("New category ID: "))
#             updated = crud.update_product(db, product_id, name, price, category_id)
#             print("Product updated." if updated else "Product not found.")

#         elif choice == "15":
#             product_id = int(input("Product ID to delete: "))
#             deleted = crud.delete_product(db, product_id)
#             print("Product deleted." if deleted else "Product not found.")

#         # --- Orders ---
#         elif choice == "16":
#             customer_id = int(input("Customer ID: "))
#             items = []
#             print("Enter product IDs and quantities (blank product ID to finish):")
#             while True:
#                 prod_id = input("Product ID: ").strip()
#                 if not prod_id:
#                     break
#                 quantity = int(input("Quantity: "))
#                 items.append({"product_id": int(prod_id), "quantity": quantity})
#             order = crud.create_order(db, customer_id, items)
#             print(f"Order placed with ID {order.id}")

#         elif choice == "17":
#             orders = crud.get_all_orders(db)
#             for order in orders:
#                 print(f"Order ID {order.id} - Customer {order.customer_id} - Date {order.order_date}")
#                 for item in order.order_items:
#                     print(f"  Product {item.product_id} - Qty: {item.quantity}")

#         elif choice == "18":
#             order_id = int(input("Order ID: "))
#             order = crud.get_order_by_id(db, order_id)
#             if order:
#                 print(f"Order ID: {order.id}, Customer ID: {order.customer_id}, Date: {order.order_date}")
#                 for item in order.order_items:
#                     print(f"  Product {item.product_id}, Quantity: {item.quantity}")
#             else:
#                 print("Order not found.")

#         elif choice == "19":
#             order_id = int(input("Order ID to update: "))
#             order = crud.get_order_by_id(db, order_id)
#             if not order:
#                 print("Order not found.")
#                 continue
#             print("Current order items:")
#             for item in order.order_items:
#                 print(f"Product ID: {item.product_id}, Qty: {item.quantity}")

#             new_items = []
#             print("Enter new product IDs and quantities (blank product ID to finish):")
#             while True:
#                 prod_id = input("Product ID: ").strip()
#                 if not prod_id:
#                     break
#                 quantity = int(input("Quantity: "))
#                 new_items.append({"product_id": int(prod_id), "quantity": quantity})

#             updated = crud.update_order_items(db, order_id, new_items)
#             print("Order updated." if updated else "Failed to update order.")

#         elif choice == "20":
#             order_id = int(input("Order ID to delete: "))
#             deleted = crud.delete_order(db, order_id)
#             print("Order deleted." if deleted else "Order not found.")

#         elif choice == "0":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option, please try again.")

#     db.close()

# if __name__ == "__main__":
#     main()
