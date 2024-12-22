from tkinter import *
from fpdf import FPDF

root=Tk()
root.title("Invoice Generator")
medicines={
    "Medicine 1 ":100,
    "Medicine 2 ":200,
    "Medicine 3":50,
    "Medicine 4":300,
    "Medicine 5":90
}#this is the dictinory  beacuse it can save both val and

invoice_items=[]

def add_medicine():
    selected_medicine = medicine_list.get(ANCHOR)#here anchor is used to get the one whom user click on
    total_quantity=int(quantity_entry.get())
    price=medicines[selected_medicine]# to get the the price odf the specific medicine we list[name whose value we needed]
    grand_total = price * total_quantity
    invoice_items.append((selected_medicine , total_quantity , grand_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

def calculate_total():# to generate sum of the bill
    total=0.0
    for item in invoice_items:#so that all the pervious and new item get added
        total = total + item[2]
    return total

def update_invoice_text():
    invoice_text.delete(1.0,END)#we delete this because all the previous  content will be delete
    for item in invoice_items:#go through the each item in the invoice_items
        invoice_text.insert(END,f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")


def generate_invoice():
    customer_name=customer_name_entry.get()

    pdf =FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica",size=12)

    pdf.cell(0,10,text='INVOICE',new_x="LMARGIN",new_y="NEXT",align="C")
    pdf.cell(0,10,text=customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,text="",new_x="LMARGIN",new_y="NEXT")
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0,10,text=f"Medicine: {medicine_name}, Quantity: {quantity}, Item: {item_total}",new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,text="Total Amount:"+ str(calculate_total()),new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.output("invoice.pdf")

medicine_label=Label(root,text="Medicine: ")
medicine_label.pack()

medicine_list=Listbox(root,selectmode=SINGLE)
for medicine in medicines:
    medicine_list.insert(END,medicine)
medicine_list.pack()

quantity_label=Label(root,text="Quantity")
quantity_label.pack()

quantity_entry=Entry(root)
quantity_entry.pack()

add_button=Button(root,text="Add Medicine",command=add_medicine)
add_button.pack()

total_amount_label=Label(root,text="Total Amount")
total_amount_label.pack()
total_amount_entry=Entry(root)
total_amount_entry.pack()

customer_name_label=Label(root,text="customer_name_label")
customer_name_label.pack()

customer_name_entry=Entry(root)
customer_name_entry.pack()

generate_button=Button(root,text="Generate Invoice",command=generate_invoice)
generate_button.pack()


invoice_text=Text(root,height=10,width=70)
invoice_text.pack()









root.mainloop()









