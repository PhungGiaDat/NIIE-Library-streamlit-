import streamlit as st
from module.member import MEMBER
from module.member import USER
from database.Query import insert,select


def register(submitted,member,user):
    if submitted:
        query = ("Insert into LIBRARY_USER (USERID,USERNAME,USER_PASSWORD,MEMBER_ID,ADMIN_ROLE "
                 "VALUES (%s,%s,%s,%s,%s")
        data = ()
        insert(query,data)


def sign_in(MEMBER):
    query = f"Select from LIBRARY USER where username = {MEMBER.username} and password = {MEMBER.password}"
    check = select(query)



def app():
    st.title("Welcome to :blue[NIIE Library] 📚 ")
    option = st.selectbox("Select an option Login/Signup", ["Login", "Register"])
    if option == "Login":
        with st.form(key="Login Form"):
            MEMBER.username = st.text_input("Username")
            MEMBER.password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

            if submitted:
                st.write("Username: ", MEMBER.username)
                st.write("Password: ", MEMBER.password)
    else:
        with st.form(key="Register Form"):
            user_id = st.text_input("Student ID",placeholder="Put in student ID")
            username = st.text_input("Username", placeholder="Username")
            email = st.text_input("Email", type="default", placeholder="Email")
            password = st.text_input("Password", type="password", placeholder="Password",
                                     help="Password must at least 8 characters")
            confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Confirm Password",
                                         help="Password must at least 8 characters")
            submitted = st.form_submit_button("Register")
            if password != confirm_pass:
                st.error("Password incorrect")
                return
            else:
                if submitted:
                    st.write("Username: ", username)
                    st.write("Password: ", password)
                    st.write("Confirm Password: ", confirm_pass)


if __name__ == "__main__":
    app()


