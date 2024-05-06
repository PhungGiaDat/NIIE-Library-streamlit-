import datetime

import streamlit as st
from module.books import BOOKS 
from module.member import MEMBER
from module.loan_ticket import loan_ticket
from database.Query import insert, update


def app():
    st.title("Loan Books Page ")
    members = MEMBER( 0,'','','','')
    books = BOOKS('','','','','',True)
    ticket = loan_ticket(0,'', datetime.datetime.now(),datetime.datetime.now(),'')
    with st.form(key="member ID", clear_on_submit=True):
        members.member_id = st.text_input("Member ID")
        members.member_name = st.text_input("Name : ")
        members.gender = st.text_input("Gender : ", placeholder="M/F")
        members.email = st.text_input("Email : ")    
        members.phone = st.text_input("Phone : ")
        books.book_id = st.text_input("Book ID : ",placeholder="Enter Book ID")
        books.book_name = st.text_input("Book Name : ", placeholder="Enter Book Name")
        books.book_quantity = st.number_input("Quantity : ", value=1,min_value=1,max_value=10,step=1,key=None)
        ticket.RECEIVING_TIME = st.date_input("Receiving time  : ", value=datetime.datetime.now(),min_value=datetime.datetime.now(),max_value=None,key=None)
        ticket.PAYMENT_TIME = st.date_input("Payment Time : ", min_value=ticket.RECEIVING_TIME, max_value=None, key=None)
        
        submitted = st.form_submit_button("Submit")
    try:
        if submitted:
            insert_ticket_query = "INSERT INTO LOAN_TICKET (MEMBER_NAME,RECEIVING_TIME,PAYMENT_TIME,QUANTITY_BOOKS) VALUES (%s,%s,%s,%s)"
            data = (members.member_name, ticket.RECEIVING_TIME, ticket.PAYMENT_TIME, books.book_quantity)
            insert(insert_ticket_query, data)
        else:
            print("None data")
    except Exception as er :
        print("There are values incorrect")
    st.write("outside the form")


if __name__ == "__main__":
    app()
    