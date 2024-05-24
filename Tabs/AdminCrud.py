import streamlit as st
from streamlit_option_menu import option_menu
from database.Query import insert, select,update,remove
from module.member import MEMBER
from module.books import BOOKS
from module.loan_ticket import loan_ticket
 
            
def app():
    select = option_menu(None,["Member","Books","Ticket"],
                      default_index=0,
                      icons=["person-circle","book","file-earmark-text","ticket "],
                      orientation="horizontal",)
    if select == "Member":
        member = MEMBER()
        member.member_crud()
    if select == "Books":
        new_book = BOOKS()
        new_book.book_crud()
    if select == "Ticket": 
        ticket = loan_ticket()
        ticket.loan_ticket_crud()
    
if __name__ == "__main__":
    app()



