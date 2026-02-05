import streamlit as st
from fpdf import FPDF #python module to create pdfs
import base64

                 
imagelink = 'shakeshack.png'

image1, image2, image3 = st.columns([1,3,1])

with image1:
    st.image(imagelink)

with image3:
    st.header(':green[Invoice]')

name1,name2 = st.columns(2)

with name1:
    st.write(':green[Shake Shack LTD]')
    st.write(':green[+852 2522 5608]')
    st.write(":green[Two International Finance Centre,]")
    st.write(':green[Central,Hong Kong.]')
    st.write('')
    st.write(':green[**Bill To**:]')


col1,col2,col3 = st.columns(3)

with col1:      
    cname = st.text_input("Enter customer name",placeholder='Enter customer name',label_visibility='collapsed')
    cemail = st.text_input("Enter email",placeholder='Enter email address',label_visibility='collapsed')

with col2:
     st.write(':green[Invoice#:]')
     st.write('')
     st.write(':green[Invoice date:]')
     st.write('')
     st.write(':green[Due date#:]')

with col3:
    invoicenum= st.number_input('invoice number',label_visibility='collapsed')
    invoiced = st.text_input('invoice date',label_visibility='collapsed')
    duedate = st.text_input('due date',label_visibility='collapsed')


des1,des2,des3,des4 = st.columns(4)


with des1:
    st.write(':green[Description:]')
    description = st.text_input('desribe',label_visibility='collapsed')


with des2:
    st.write(':green[Quantity:]')
    quantity = st.number_input('quantity',0,label_visibility='collapsed')


with des3:
    st.write(':green[Price|Unit:]')
    unitprice = st.number_input('unitprice',0,label_visibility='collapsed')



with des4:
    st.write(':green[Total Price:]')
    total = quantity * unitprice
    totalprice = st.text_input('totalprice',placeholder=f'${total:,}',label_visibility='collapsed',disabled=True)


st.divider()

pay1,pay2 = st.columns(2)


with pay1:
    st.write(':green[Payment info:]')
    st.write(':green[Acc Name: Shakeshack]')
    st.write(':green[Acc Number: 509 173 1594]')
    st.write(':green[Bank Name: UAE bank]')

with pay2:
    st.write(':green[Payment Due]')
    st.header(f':green[${total:,}]')


def generate_pdf():
    pdf = FPDF()

    pdf.add_page()

    colX = 10
    colY = 30

    pdf.image(imagelink,x=colX,y=colY,w=20)


    pdf_file = 'shakeshack.pdf'
    pdf.output(pdf_file)
    return pdf_file



call_pdf = generate_pdf()

with open(call_pdf,'rb') as binary:
    pdf_data = binary.read()


if st.button('View Invoice'):
    write_pdf = base64.b64encode(pdf_data).decode('utf-8')


    view_pdf = f'<embed src="data:application/pdf;base64", {write_pdf}"type="application/pdf" width = "100%" height = "600px" />'

    st.markdown(view_pdf,unsafe_allow_html=True)
    