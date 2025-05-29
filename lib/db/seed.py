import sys
import os

# Add the root of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from lib.db.database import SessionLocal, engine
from lib.db import models
from lib.db.crud import (
    create_customer,
    create_category,
    create_product,
    create_order
)

# Create all tables
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data (optional)
db.query(models.OrderItem).delete()
db.query(models.Order).delete()
db.query(models.Product).delete()
db.query(models.Category).delete()
db.query(models.Customer).delete()
db.commit()

# Seed customers
customers = [
    create_customer(db, name="Alice Johnson", email="alice@example.com"),
    create_customer(db, name="Bob Smith", email="bob@example.com"),
]

# Seed categories
categories = [
    create_category(db, name="Electronics"),
    create_category(db, name="Books"),
    create_category(db, name="Clothing")
]

# Seed products
products = [
    create_product(db, name="Laptop", price=999999.99, category_id=categories[0].id),
    create_product(db, name="Headphones", price=1999.99, category_id=categories[0].id),
    create_product(db, name="Novel", price=3000.00, category_id=categories[1].id),
    create_product(db, name="T-Shirt", price=24.99, category_id=categories[2].id)
]

# Seed orders
create_order(db, customer_id=customers[0].id, items=[
    {"product_id": products[0].id, "quantity": 1},
    {"product_id": products[2].id, "quantity": 2},
])

create_order(db, customer_id=customers[1].id, items=[
    {"product_id": products[1].id, "quantity": 1},
    {"product_id": products[3].id, "quantity": 3},
])

db.close()

print("✅ Database seeded successfully!")
