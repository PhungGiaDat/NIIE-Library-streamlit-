
import streamlit as st
from module.loan_ticket import loan_ticket


def app():
    st.title("Loan Books Page ")
    ticket = loan_ticket()
    ticket.loan_books_tab()


    st.write("If you want to loan more books, please fill the form again")


if __name__ == "__main__":
    app()
