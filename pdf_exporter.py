from fpdf import FPDF

def export_invoice(invoice_id, customer_name, product_name, price, quantity):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Invoice ID: {invoice_id}", ln=True)
    pdf.cell(200, 10, txt=f"Customer: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Product: {product_name}", ln=True)
    pdf.cell(200, 10, txt=f"Price: {price}", ln=True)
    pdf.cell(200, 10, txt=f"Quantity: {quantity}", ln=True)
    pdf.cell(200, 10, txt=f"Total: {price * quantity}", ln=True)

    filename = f"invoice_{invoice_id}.pdf"
    pdf.output(filename)
    print(f"Invoice exported to {filename}")
