from sqlalchemy.orm import sessionmaker
from db.models import engine, Customer, Product, Category, Order, OrderItem

Session = sessionmaker(bind=engine)
session = Session()

    #Code Validation
# Print all customers check
def list_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"ID: {customer.id} | Name: {customer.name} | Email: {customer.email}")

#  Add a new customer
def add_customer(name, email):
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    print(f"Added customer {name}.")

#  Print all products
def list_products():
    products = session.query(Product).all()
    for product in products:
        print(f"{product.name} - ${product.price}")

# Run code 
if __name__ == "__main__":
    print("Debug CLI for E-commerce App")
    print("=" * 40)

    # Call 
    list_customers()
    list_products()