import datetime
import streamlit as st
import time
import pymysql
from database.Query import insert, select, update


class loan_ticket():
    ## TICKET TABLE
    TICKET_ID = 0
    MEMBER_ID = ""
    MEMBER_NAME = ""
    ADDRESS = ""
    PHONE = ""
    RECEIVING_TIME = datetime.datetime.now()
    PAYMENT_TIME = datetime.datetime.now()
    
    ## TICKET_DETAILS TABLE
    BOOK_NAME = ""
    BOOK_QUANTITY = 0
    STATUS = ["ON LOAN","PAID"]
    
    ## This function checks if the receiving time is less than the payment time
    def check_time(self): 
        if self.RECEIVING_TIME > self.PAYMENT_TIME:
            return True
        else:
            return False
        
    def check_book_availability(self):
        query = f"SELECT status FROM BOOKS WHERE BOOKS_TITLE = '{self.BOOK_NAME}'"
        data = select(query)
        print(data)
        for check in range(len(data)):
            if check == 'AVAILABLE':
                return True
            else:
                st.error("Book not found or Out Of Stock")
                return False

    def handle_loan_ticket (self):
        if self.check_time():  # Assuming payment_time and receiving_time attributes exist
            st.error("Payment time cannot be earlier than receiving time.")
        else:
            insert_ticket_query = (
                "INSERT INTO LOAN_TICKET (MEMBER_ID,MEMBER_NAME,RECEIVING_TIME,PAYMENT_TIME) "
                "VALUES (%s,%s,%s,%s)")
            data = (self.get_member_id,self.MEMBER_NAME, self.RECEIVING_TIME, self.PAYMENT_TIME)
            
            if all(item is not None for item in data):
                with st.spinner("Moment will take a while"):
                    time.sleep(2)
                    try:
                        insert(insert_ticket_query, data)
                    except pymysql.Error as err:
                        st.error(f"Error: {err}")
                    finally:
                        try:
                            self.insert_ticket_details()
                        except pymysql.Error as err:
                            st.error(err)
                        finally:
                            st.success("Loan Ticket added successfully")
            else:   
                st.error("Please fill all the information")

    def insert_ticket_details(self):
        query = "INSERT INTO TICKET_DETAILS (BOOKS_ID,BOOKS_TITLE,QUANTITY_BOOKS,MEMBER_ID) VALUES (%s,%s,%s,%s)"
        data = (self.get_book_id,self.BOOK_NAME, self.BOOK_QUANTITY,self.get_member_id)
        insert(query, data)


    def loan_ticket_crud(self):
        tab1, tab2, tab3, tab4 = st.tabs(["Add ticket", "Update ticket", "Delete ticket", "View ticket"])

        with tab1:
            self.loan_books_tab()
        with tab2:
            self.update_ticket_tab()
        with tab3:
            pass
        with tab4:
            self.view_ticket_tab()
        
    ## phieu muon     
    def loan_books_tab(self):
        with st.form(key="insert ticket", clear_on_submit=True):
            self.MEMBER_NAME = st.text_input("Name  ", placeholder="Enter Your Full-Name")
            self.ADDRESS = st.text_input("Address  ", placeholder="Street, District, City, Country")
            self.PHONE = st.text_input("Phone  ", placeholder="Phone Number")
            self.BOOK_NAME = st.text_input("Book Name  ", placeholder="Enter Book Name")
            self.BOOK_QUANTITY = st.number_input("Books Quantity  ", value=1, min_value=1, max_value=10, step=1,
                                                   key=None)
            self.RECEIVING_TIME = st.date_input("Receiving time   ", min_value=datetime.datetime.now(), key=None)
            self.PAYMENT_TIME = st.date_input("Payment Time  ", min_value=self.RECEIVING_TIME, key=None,
                                                help="Payment Time Much Higher Than Received Time")

            submitted = st.form_submit_button("Submit")
            # If user submitted call handle_loan_ticket function
        if submitted:
            if self.check_book_availability():
                self.handle_loan_ticket()
            else:
                st.error("Book not found or Out Of Stock")
        else:
            st.warning("Please fill all the information")

    
    def update_ticket_tab(self):
            st.write("Update Ticket")
            with st.form(key="Update Ticket"):
                self.TICKET_ID = st.text_input("Ticket ID", placeholder="Put in Ticket ID")
                self.MEMBER_NAME = st.text_input("Name  ", placeholder="Enter Your Full-Name")
                self.BOOK_NAME = st.text_input("Book Name  ", placeholder="Enter Book Name")
                self.BOOK_QUANTITY = st.number_input("Books Quantity  ", value=1, min_value=1, max_value=10, step=1,
                                                    key=None)
                self.RECEIVING_TIME = st.date_input("Receiving time   ", min_value=datetime.datetime.now(), key=None)
                self.PAYMENT_TIME = st.date_input("Payment Time  ", min_value=self.RECEIVING_TIME, key=None,
                                                    help="Payment Time Much Higher Than Received Time")
                self.STATUS = st.selectbox("Status", ["ON LOAN", "PAID"])
                submit = st.form_submit_button("Update Ticket")
                if submit:
                    try:
                        query = ("UPDATE LOAN_TICKET SET MEMBER_NAME = %s, ADDRESS = %s, BOOK_TITLE= %s , BOOK_QUANTITY = %s ,RECEIVING_TIME = %s,PAYMENT_TIME =%s ,WHERE TICKET_ID = %s")
                        tk_details_query = ("UPDATE TICKET_DETAILS SET STATUS = %s WHERE TICKET_ID = %s")
                        data = (self.MEMBER_NAME, self.ADDRESS, self.BOOK_NAME, self.BOOK_QUANTITY, self.RECEIVING_TIME, self.PAYMENT_TIME, self.TICKET_ID)
                        tk_data = (self.STATUS, self.TICKET_ID)
                        update(query, data)
                    except pymysql.Error as err:
                        st.error(f"Error: {err}")
                    finally:
                        try:
                            update(tk_details_query, tk_data)
                        except pymysql.Error as err:
                            st.error(err)
                        finally:
                            st.success("Update Member Success")
                            
    def view_ticket_tab(self):
        query = "SELECT * FROM LOAN_TICKET JOIN TICKET_DETAILS ON LOAN_TICKET.TICKET_ID = TICKET_DETAILS.TICKET_ID"
        data = select(query)
        st.table(data)
        
    def get_member_id(self):
        query = "SELECT MEMBER_ID FROM LIBRARY_MEMBER WHERE MEMBER_NAME = %s"
        data = (self.MEMBER_NAME)
        member_id = select(query, data)
        if member_id:
            return member_id
        else:
            st.error("Member not found")
            return None
    def get_book_id(self):
        query = "SELECT BOOKS_ID FROM BOOKS WHERE BOOKS_TITLE = %s"
        data = (self.BOOK_NAME)
        book_id = select(query, data)
        if book_id:
            return book_id
        else:
            st.error("Book not found")
            return None