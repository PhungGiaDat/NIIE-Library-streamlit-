import streamlit as st
import pymysql
from streamlit_option_menu import option_menu
from database.Query import insert, select, update, remove

class MEMBER():
    member_name = ""
    gender = ""
    email = ""
    phone = ""  
    address = ""
    
    user_name = ""
    user_password = ""
    admin_role = False
    
    confirm_password = ""
    
    def check_phonenumber(self):
        if len(self.phone) != 10:
            return False
        return True
    
    def member_crud(self):
        tab1, tab2, tab3, tab4 = st.tabs(["Add Member", "Update Member", "Delete Member", "View Member"])
        
        with tab1:
            self.add_member_tab()
        with tab2:
            self.update_member_tab()
        with tab3:
            self.delete_member_tab()
        with tab4:
            self.view_member_tab()

    def add_member_tab(self):
        st.write("Add Member")
        with st.form(key="Add Member"):
            st.header("Member Information")
            self.member_name = st.text_input("Name", placeholder="Name")
            self.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            self.email = st.text_input("Email", placeholder="Email")
            self.phone = st.text_input("Phone", placeholder="Phone")
            self.address = st.text_input("Address", placeholder="Address")
            st.markdown("-----------------------------")
            st.header("User Account")
            self.user_name = st.text_input("Username",placeholder="username")
            self.user_password = st.text_input("Password",type="password",placeholder="password")
            submit = st.form_submit_button("Add Member")
            if submit and self.check_phonenumber():
                try:
                    self.insert_user()
                except pymysql.Error as err:
                    st.error(f"Error: {err}")
                finally:
                    st.success("Add Member Success")


    def update_member_tab(self):
        st.write("Update Member")
        with st.form(key="Update Member"):
            name = st.text_input("Name", placeholder="Name")
            email = st.text_input("Email", placeholder="Email")
            phone = st.text_input("Phone", placeholder="Phone")
            address = st.text_input("Address", placeholder="Address")
            submit = st.form_submit_button("Update Member")

            if submit and self.check_phonenumber():
                try:
                    query = "UPDATE LIBRARY_MEMBER SET NAME=%s, EMAIL=%s, PHONE=%s, ADDRESS=%s WHERE STUDENT_ID=%s"
                    data = (name, email, phone, address)
                    update(query, data)
                except pymysql.Error as err:
                    st.error(f"Error: {err}")
                finally:
                    st.success("Update Member Success")

    def delete_member_tab(self):
        st.write("Delete Member")
        with st.form(key="Delete Member"):
            student_id = st.text_input("Student ID", placeholder="Put in student ID")
            submit = st.form_submit_button("Delete Member")
            if submit:
                query = "DELETE FROM LIBRARY_MEMBER WHERE STUDENT_ID=%s"
                data = (student_id,)
                remove(query, data)
                st.success("Delete Member Success")

    def view_member_tab(self):
        st.write("View Member")
        query = "SELECT * FROM LIBRARY_MEMBER"
        data = select(query)
        st.table(data)
        
    def insert_user(self):
        try:
            # Insert user data
            user_query = "INSERT INTO LIBRARY_USER (username, user_password, admin_role) VALUES (%s, %s, %s)"
            user_data = (self.user_name, self.user_password, 0)  # Assuming default user role is 0 (not admin)
            insert(user_query, user_data)

            # Insert member data
            query = "INSERT INTO LIBRARY_MEMBER (MEMBER_NAME, MEMBER_GENDER, MEMBER_EMAIL, MEMBER_PHONENUMBER, MEMBER_ADDRESS) VALUES (%s, %s, %s, %s, %s)"
            data = (self.member_name, self.gender, self.email, self.phone, self.address)
            insert(query, data)

        except pymysql.Error as err:
            st.error(f"Error: {err}")
            print(err)
    
    def register(self):
        st.write("Add Member")
        with st.form(key="Add Member"):
            st.header("Member Information")
            self.member_name = st.text_input("Name", placeholder="Name")
            self.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            self.email = st.text_input("Email", placeholder="Email")
            self.phone = st.text_input("Phone", placeholder="Phone")
            self.address = st.text_input("Address", placeholder="Address")
            st.markdown("-----------------------------")
            st.header("User Account")
            self.user_name = st.text_input("Username",placeholder="username")
            self.user_password = st.text_input("Password",type="password",placeholder="password")
            self.confirm_password = st.text_input("Confirm Password",type="password",placeholder="confirm password")
            submit = st.form_submit_button("Add Member")
            if submit and self.check_phonenumber() and self.user_password == self.confirm_password:
                try:
                    self.insert_user()
                except pymysql.Error as err:
                    st.error(f"Error: {err}")
                finally:
                    st.success('Registration successful! You can now log in')
       
    