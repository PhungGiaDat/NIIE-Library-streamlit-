import streamlit as st 


def app():
    st.title("Loan Books Page ")
    
    with st.form(key="member ID", clear_on_submit=True):
        member_id = st.text_input("Member ID")
        member_name = st.text_input("Name : ")
        member_gender = st.text_input("Gender : ",placeholder="M/F")
        member_email = st.text_input("Email : ")    
        member_phone = st.text_input("Phone : ")
        book_id= st.text_input("Book ID : ",placeholder="Enter Book ID")
        book_name = st.text_input("Book Name : ",placeholder="Enter Book Name") 
        book_quantity = st.number_input("Quantity : ",value=1,min_value=1,max_value=10,step=1,key=None)
        date_issued = st.date_input("Date Issued : ",value=None,min_value=None,max_value=None,key=None)
        date_due = st.date_input("Date Due : ",value=date_issued,min_value =date_issued,max_value=None,key=None)       
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Member ID : ",member_id)
            st.write("Name : ",member_name)
    st.write("outside the form")
if __name__ == "__main__":
    app()
    