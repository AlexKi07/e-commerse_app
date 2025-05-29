
from sqlalchemy.orm import Session
from . import models
from datetime import datetime

# ----------------- Customer CRUD -----------------
def create_customer(db: Session, name: str, email: str):
    customer = models.Customer(name=name, email=email)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_all_customers(db: Session):
    return db.query(models.Customer).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, name: str, email: str):
    customer = get_customer_by_id(db, customer_id)
    if customer:
        customer.name = name
        customer.email = email
        db.commit()
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer

# ----------------- Category CRUD -----------------
def create_category(db: Session, name: str):
    category = models.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_all_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, name: str):
    category = get_category_by_id(db, category_id)
    if category:
        category.name = name
        db.commit()
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category

# ----------------- Product CRUD -----------------
def create_product(db: Session, name: str, price: float, category_id: int):
    product = models.Product(name=name, price=price, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, name: str, price: float, category_id: int):
    product = get_product_by_id(db, product_id)
    if product:
        product.name = name
        product.price = price
        product.category_id = category_id
        db.commit()
    return product

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product

# ----------------- Order and OrderItem CRUD -----------------
def create_order(db: Session, customer_id: int, items: list):
    """
    items: list of dicts, e.g., [{'product_id': 1, 'quantity': 2}, ...]
    """
    order = models.Order(customer_id=customer_id, order_date=datetime.utcnow())
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in items:
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity']
        )
        db.add(order_item)
    db.commit()
    db.refresh(order)
    return order

def get_all_orders(db: Session):
    return db.query(models.Order).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update_order_items(db: Session, order_id: int, items: list):
    """
    Overwrites all existing order items.
    items: list of dicts like [{'product_id': 1, 'quantity': 3}]
    """
    order = get_order_by_id(db, order_id)
    if not order:
        return None
    # Delete old items
    db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).delete()
    # Add new items
    for item in items:
        new_item = models.OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity']
        )
        db.add(new_item)
    db.commit()
    return order

def delete_order(db: Session, order_id: int):
    order = get_order_by_id(db, order_id)
    if order:
        db.delete(order)
        db.commit()
    return order
