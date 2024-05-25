import datetime
import pymysql
import streamlit as st
import time
from database.Query import insert, select, update, remove
class BOOKS:
    # This is the parent class for TYPE_BOOKS AND TICKET_DETAILS
    books_id = ""
    book_name = ""
    year_of_product = 0
    author = ""
    status = ["Available", "OUT_OF_STOCK"]
    genre = ''
    type_format = ''
    type_language = ''
    edition = ''

    def check_year(self): ## This function checks if the year of production is less than the current year
        if self.year_of_product < datetime.datetime.now().year:
            return True
        else:
            return False
        
    def book_crud(self):
        tab1, tab2, tab3, tab4 = st.tabs(["Add Book", "Update Book", "Delete Book", "View Book"])
        
        with tab1:
            self.add_book_tab()
        with tab2:
            self.update_book_tab()
        with tab3:
            self.delete_book_tab()
        with tab4:
            self.view_book_tab()

    def add_book_tab(self):
        st.caption("Add Book")
        with st.form(key="Add Member"):
            st.header("Add Book")
            self.book_name = st.text_input("Book Name", placeholder="Name")
            self.year_of_product = st.number_input("Year of Product", value=2021, min_value=1900, max_value=2024, step=1, key=None)
            self.author = st.text_input("Author", placeholder="Author")
            # Insert the new book into the database [TYPE_BOOKS]
            self.genre = st.text_input("Genre", placeholder="Genre")
            self.type_format = st.text_input("Type Format", placeholder="Type Format")
            self.type_language = st.text_input("Type Language", placeholder="Type Language")
            self.edition = st.text_input("Edition", placeholder="Edition")
            self.quantity = st.number_input("Quantity",min_value=1,max_value=100,step=1)
            
            
            submit = st.form_submit_button("Add book")
            if submit and self.check_year():
                try:
                    query = ("INSERT INTO books (BOOKS_TITLE,AUTHOR,YEAR_OF_PRODUCT,GENRE,TYPE_FORMAT,TYPE_LANGUAGE,EDITION,QUANTITY) "
                             "VALUES (%s, %s, %s, %s, %s,%s, %s,%s)")
                    data = (self.book_name, self.author,self.year_of_product,self.genre,self.type_format, self.type_language, self.edition,self.quantity)
                    insert(query, data)
                    # Insert the new book into the database [TYPE_BOOKS]
                except pymysql.Error as err:
                    st.error(f"Error: {err}")
                    if err is False:
                        st.success("Add Book Success")
                finally:
                    try:
                        query_tp = ("INSERT INTO BOOKS_DETAILS (STATUS) VALUES (%s)")
                        data = (self.status[0])
                        insert(query_tp, data)
                    except pymysql.Error as err:
                        st.error(err)

    def update_book_tab(self):
        st.write("Update Member")
        with st.form(key="Update Member"):
            self.books_id = st.text_input("Books ID", placeholder="Put in books ID")
            self.book_name = st.text_input("Book Title", placeholder="Name")
            self.author = st.text_input("Author", placeholder="Author")
            self.year_of_product = st.number_input("Year of Product", value=2021, min_value=1900, max_value=2024, step=1, key=None)
            self.genre = st.text_input("Genre", placeholder="Genre")
            self.type_format = st.text_input("Type Format", placeholder="Type Format")
            self.type_language = st.text_input("Type Language", placeholder="Type Language")
            self.edition = st.text_input("Edition", placeholder="Edition")
            submit = st.form_submit_button("Update Member")
            if submit:
                try:
                    query = "UPDATE BOOKS SET BOOKS_TITLE=%s, AUTHOR=%s, YEAR_OF_PRODUCT=%s, GENRE=%s, TYPE_FORMAT=%s, TYPE_LANGUAGE=%s, EDITION=%s WHERE BOOKS_Id=%s"
                    data = (self.book_name, self.author, self.year_of_product, self.genre, self.type_format, self.type_language, self.edition, self.books_id)
                    update(query, data)
                except pymysql.Error as err:
                    st.error(f"Error: {err}")
                finally:
                    st.success("Update Member Success")

    def delete_book_tab(self):
        st.write("Delete Books")
        with st.form(key="Delete Books"):
            self.books_id = st.text_input("Books ID", placeholder="Put in books ID")
            self.book_name = st.text_input("Book Name", placeholder="Name")
            submit = st.form_submit_button("Delete Member")
            if submit:
                query = "DELETE FROM LIBRARY_MEMBER WHERE BOOKS_Id=%s and BOOKS_TITLE=%s"
                data = (self.books_id, self.book_name)
                remove(query, data)
                st.success("Delete Member Success")

    def view_book_tab(self):
        st.write("View all of books in library stock")
        query = "SELECT * FROM BOOKS"
        data = select(query)
        st.table(data)
    

        
        
        