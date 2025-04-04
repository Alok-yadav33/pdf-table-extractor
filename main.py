from db import setup_database
from invoice_utils import *
from pdf_exporter import export_invoice

setup_database()

print("==== Invoice Management System ====")
username = input("Enter admin username: ")
password = input("Enter password: ")

if login(username, password):
    print("Login successful.\n")
    while True:
        print("\n1. Add Customer\n2. Add Product\n3. Create Invoice\n4. View Invoices\n5. Export Invoice to PDF\n6. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            name = input("Customer Name: ")
            email = input("Email: ")
            add_customer(name, email)
            print("Customer added.")
        
        elif choice == '2':
            name = input("Product Name: ")
            price = float(input("Price: "))
            add_product(name, price)
            print("Product added.")

        elif choice == '3':
            customers = view_customers()
            products = view_products()

            print("Customers:")
            for c in customers:
                print(f"{c[0]} - {c[1]}")
            customer_id = int(input("Choose Customer ID: "))

            print("Products:")
            for p in products:
                print(f"{p[0]} - {p[1]} @ ₹{p[2]}")
            product_id = int(input("Choose Product ID: "))
            quantity = int(input("Quantity: "))

            create_invoice(customer_id, product_id, quantity)
            print("Invoice created.")

        elif choice == '4':
            invoices = view_invoices()
            for inv in invoices:
                print(f"ID: {inv[0]}, Customer: {inv[1]}, Product: {inv[2]}, Qty: {inv[4]}, Total: ₹{inv[3]*inv[4]}")
        
        elif choice == '5':
            invoices = view_invoices()
            for inv in invoices:
                print(f"{inv[0]}: {inv[1]} - {inv[2]}")
            invoice_id = int(input("Enter invoice ID to export: "))
            for inv in invoices:
                if inv[0] == invoice_id:
                    export_invoice(*inv)
                    break

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
else:
    print("Login failed.")
