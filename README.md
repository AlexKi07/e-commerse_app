#  E-Commerce CLI App

This app is a command-line-based E-commerce management system for handling customers, products, categories, orders, and order items. Built using SQLAlchemy ORM and Alembic, this app allows full CRUD operations and tracks relationships between various entities within a store environment, e.g, customers, orders, and products.

## 📦 Description

This project simulates a backend for an E-commerce platform. Users can manage inventory and process orders entirely from the terminal using a user-friendly CLI interface. It showcases object-relational modeling, CRUD logic, database migrations, and modular Python project structuring.

##  Author

**Alex Kimani**

## ⚙️ Setup Instructions

1. **Clone the repository**  
   git clone https://github.com/AlexKi07/e-commerse_app.git
   cd e-commerse_app

2. **Install dependencies using Pipenv**
    pipenv install
    pipenv shell

3. **Run migrations**
    alembic upgrade head

4. **Seed the database (optional)**
    python lib/seed.py

5. **Start the CLI**
    python lib/main.py


# Features
1. Add, view, update, and delete customers
2. Create and manage products and categories
3. Place and review customer orders
4. Add and remove items from orders
5. View customer order history
6. Search and filter through data with easy prompts
7. Error handling and input validation

# Technologies Used
1. Python 3.8+
2. SQLAlchemy (ORM)
3. Alembic (migrations)
4. SQLite (database)
5. Pipenv (environment manager)

# Support
For questions or feedback, contact Alex Kimani at:
Email:kimanialexk07@gmail.com
Phone No.:0769644400


**📄 License**
MIT License

Copyright 2025 Alex Kimani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

© 2025 Alex Kimani
