from db import get_connection

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result is not None

def add_customer(name, email):
    conn = get_connection()
    conn.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def add_product(name, price):
    conn = get_connection()
    conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def create_invoice(customer_id, product_id, quantity):
    conn = get_connection()
    conn.execute("INSERT INTO invoices (customer_id, product_id, quantity) VALUES (?, ?, ?)",
                 (customer_id, product_id, quantity))
    conn.commit()
    conn.close()

def view_customers():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM customers").fetchall()
    conn.close()
    return rows

def view_products():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return rows

def view_invoices():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT invoices.id, customers.name, products.name, products.price, invoices.quantity
        FROM invoices
        JOIN customers ON invoices.customer_id = customers.id
        JOIN products ON invoices.product_id = products.id
    ''')
    result = cursor.fetchall()
    conn.close()
    return result
