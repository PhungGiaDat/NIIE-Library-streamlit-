import streamlit as st 
import pymysql
import threading
from streamlit_option_menu import option_menu
from Tabs import Homepage ,Loan_books, Books,AdminCrud
from database.Query import select
from module.member import MEMBER

st.set_page_config(
    page_title="NIIE Library", 
    page_icon=":book:"
)


class MultiApp:
    def run(self):
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if "user_role" not in st.session_state:
            st.session_state.user_role = None

        if not st.session_state.logged_in:
            self.show_login_signup()
        else:
            if st.session_state.user_role == 1:
                self.admin_form()
            elif st.session_state.user_role == 0:
                self.user_form()
            else:
                st.sidebar.info("Please login to continue.")

    def show_login_signup(self):
        st.sidebar.title("Login/Signup")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        login_button = st.sidebar.button("Login",key="login")
        st.sidebar.info("Dont have a account ?")
        sign_up_button = st.sidebar.button("Sign Up", key="signup", help="Create an account")

        if sign_up_button:
            self.__sign_up()

        if login_button:
            self.__sign_in(username, password)
            st.rerun()
    
    def __sign_up(self):
        new_member = MEMBER()
        if "form_submitted" not in st.session_state:
            st.session_state.form_submitted = False

        if st.session_state.form_submitted:
            st.info("Form already submitted. Please log in.")
            return

        new_member = MEMBER()
        if new_member.register():
            st.session_state.form_submitted = True
            
    @staticmethod
    def __sign_in(username,password):
        try:
            query = f"SELECT username, user_password, admin_role FROM library_user WHERE username = '{username}' AND user_password = '{password}'"
            user = select(query)
            if user:
                st.sidebar.success(f"Logged in as {username}")
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.user_role = user[0][2]   # Assuming the query returns a list of tuples
            else:
                st.sidebar.error("Incorrect username or password.")
        except pymysql.Error as err:
            st.sidebar.error(f"Error: {err}")
            
    
    def __sign_out(self):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.session_state.username = None
        st.rerun()

    def admin_form(self):
        with st.sidebar.empty():
            with st.sidebar:
                app = option_menu(
                    menu_title="Admin Site",
                    options=["Homepage", "Books", "LoanBooks", "Admin"],
                    menu_icon='chat-text-fill',
                    icons=['house-fill', 'person-circle', 'book', ''],
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important", "background-color": 'white'},
                        "icon": {"color": "black", "font-size": "23px"},
                        "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "navy-blue"},
                        "nav-link-selected": {"background-color": "white"},
                    }
                )
                if st.sidebar.button("Sign Out"):
                    self.__sign_out()
                # --- App Selection ---
        if app == "Homepage":
            Homepage.app()
        elif app == "LoanBooks":
            Loan_books.app()
        elif app == "Books":
            Books.app()
        elif app == "Admin":
            AdminCrud.app()

    def user_form(self):
        with st.sidebar.empty():
            with st.sidebar:
                app = option_menu(
                    menu_title="Select App",
                    options=["Homepage", "Books", "LoanBooks","About"],
                    menu_icon='chat-text-fill',
                    icons=['house-fill', 'person-circle', 'book', 'basket'],
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important", "background-color": 'white'},
                        "icon": {"color": "black", "font-size": "23px"},
                        "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "navy-blue"},
                        "nav-link-selected": {"background-color": "white"},
                    }
                )
                if st.sidebar.button("Sign Out"):
                    self.__sign_out()
                # --- App Selection ---
        if app == "Homepage":
            Homepage.app()
            st.write("Welcome to the NIIE Library homepage.")
        elif app == "LoanBooks":
            Loan_books.app()
        elif app == "Books":
            Books.app()

# Create an instance of the MultiApp class
app = MultiApp()
# Run the app
app.run()