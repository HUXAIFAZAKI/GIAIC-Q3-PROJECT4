import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

FIXED_TAX_RATE = 10
FOOD_ITEMS = {
    "Burger": 250,
    "Pizza (S)": 400,
    "Pizza (M)": 800,
    "Pizza (L)": 1000,
    "Pasta": 400,
    "Salad": 100,
    "Soda": 70,
    "Fries": 100,
    "Sandwich": 300
}

st.set_page_config(page_title="Food Invoice Generator", page_icon="🍔", layout="centered")
st.title("🍔 Food Invoice Generator")

invoice_number = st.text_input("Invoice Number", "INV-001")
client_name = st.text_input("Customer Name", "Huzaifa")
client_phone = st.text_input("Phone Number", "0123456789")

st.sidebar.title("Invoice Settings")
discount = st.sidebar.number_input("Discount (%)", min_value=0, value=5)
num_items = st.sidebar.number_input("Number of items", min_value=1, value=1)

st.subheader("🍽️ Select Food Items")

item_data = []

for i in range(num_items):
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_item = st.selectbox(f"Item {i+1}", list(FOOD_ITEMS.keys()), key=f"item_{i}")
    with col2:
        quantity = st.number_input(f"Quantity {i+1}", min_value=1, key=f"qty_{i}")
    with col3:
        price = FOOD_ITEMS[selected_item]
        total_price = price * quantity
        st.write(f"**Price Per 1:** ${price}")
        st.write(f"**Total Price:** ${total_price}")
    item_data.append({"Description": selected_item, "Quantity": quantity, "Price": total_price})

st.markdown("---")

df = pd.DataFrame(item_data)

st.write("### 📝 Invoice Preview")
st.table(df)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 20)
        self.set_text_color(25, 25, 25) 
        self.cell(200, 10, "Food Invoice", ln=True, align='C')
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, "Thank you for dining with us!", align="C")

def generate_invoice():
    subtotal = sum(item["Quantity"] * item["Price"] for item in item_data)
    tax_amount = (subtotal * FIXED_TAX_RATE) / 100
    discount_amount = (subtotal * discount) / 100
    total = subtotal + tax_amount - discount_amount

    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, f"Invoice #{invoice_number}", ln=True, align='C')
    pdf.cell(200, 10, f"Customer: {client_name}", ln=True, align='L')
    pdf.cell(200, 10, f"Phone: {client_phone}", ln=True, align='L')
    pdf.ln(10)

    pdf.set_fill_color(25, 25, 25)  
    pdf.set_text_color(255, 255, 255) 
    pdf.cell(60, 10, "Description", border=1, fill=True)
    pdf.cell(40, 10, "Quantity", border=1, fill=True)
    pdf.cell(40, 10, "Price", border=1, fill=True)
    pdf.cell(40, 10, "Total", border=1, fill=True)
    pdf.ln()

    for item in item_data:
        pdf.set_text_color(0,0,0)
        pdf.cell(60, 10, item["Description"], border=1)
        pdf.cell(40, 10, str(item["Quantity"]), border=1)
        pdf.cell(40, 10, f"${item['Price']}", border=1)
        pdf.cell(40, 10, f"${item['Quantity'] * item['Price']}", border=1)
        pdf.ln()

    pdf.ln(10)

    pdf.set_text_color(0,0,0)
    pdf.cell(200, 10, f"Subtotal: ${subtotal}", ln=True)
    pdf.cell(200, 10, f"Tax ({FIXED_TAX_RATE:.0f}%): ${tax_amount}", ln=True)
    pdf.cell(200, 10, f"Discount ({discount:.0f}%): -${discount_amount:.0f}", ln=True)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Total: ${total:.0f}", ln=True)

    file_path = f"invoices/invoice_{invoice_number}.pdf"
    pdf.output(file_path)
    
    return file_path

if st.button("Generate Invoice PDF"):
    pdf_path = generate_invoice()
    st.success(f"Invoice saved as `{pdf_path}`")
    
    with open(pdf_path, "rb") as file:
        st.download_button("Download Invoice", file, file_name=f"invoice_{invoice_number}.pdf")