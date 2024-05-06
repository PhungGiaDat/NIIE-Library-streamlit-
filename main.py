import streamlit as st 
from streamlit_option_menu import option_menu as st_option_menu
from Tabs import Homepage, Account, Loan_books , Books


st.set_page_config(
    page_title="NIIE Library", 
    page_icon=":book:"
)


class MultiApp:
    # Class for adding multiple apps
    # Phương thức khởi tạo
    def __init__(self):
        # Create a list of apps
        self.apps = []
        
    # Phương thức hay Function thêm ứng dụng
    def add_app(self, title, func):
        # thêm vào một ứng dụng mới là dictionary
        self.apps.append
        ({
            "tilte": title,
            "function": func
        })
        
    # Function chạy ứng dụng bên sidebar
    @staticmethod
    def run():
        with st.sidebar:
            app = st_option_menu(
                menu_title="Select App",
                options=["Homepage", "Account", "Books", "Podcast", "AudioBooks", "LoanBooks", "Community", "About"],
                menu_icon='chat-text-fill',
                icons=['house-fill', 'person-circle', 'book', 'mic',
                       'headphones', 'basket', 'globe', 'info-circle-fill'],
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'white'},
                    "icon": {"color": "black", "font-size": "23px"}, 
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "navy-blue"},
                    "nav-link-selected": {"background-color": "white"},
                }
            )
        if app == "Homepage":
            Homepage.app()    
        if app == "Account":
            Account.app()
        if app == "LoanBooks":
            Loan_books.app()
        if app == "Books":
            Books.app()
    run()
        