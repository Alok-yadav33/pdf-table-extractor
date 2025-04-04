import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_excel):
    tables_list = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table_index, table in enumerate(tables):
                df = pd.DataFrame(table)
                tables_list.append(df)
    
    if tables_list:
        with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
            for idx, df in enumerate(tables_list):
                df.to_excel(writer, sheet_name=f"Table_{idx+1}", index=False, header=False)
        print(f"✅ Tables extracted and saved to {output_excel}")
    else:
        print("❌ No tables found in the PDF.")

# Example Usage
pdf_file = "sample.pdf"  # Change to your PDF file path
output_excel = "output.xlsx"
extract_tables_from_pdf(pdf_file, output_excel)
