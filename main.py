import streamlit as st 
from streamlit_option_menu import option_menu as st_option_menu
from Tabs import Homepage


st.set_page_config(
    page_title="NIIE Library", 
    page_icon=":book:"
)

# cSpell:ignore streamlit NIIE Phương thức khởi thêm ứng dụng tilte chạy bên backicon

class Multi_App:
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
    def run():
        with st.sidebar:
            app = st_option_menu(
                menu_title="Select App",
                options = ["Homepage", "Account ","Books" ,"Podcast","AudioBooks","Community","About"],
                menu_icon ='chat-text-fill',
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill','info-circle-fill','info-circle-fill'],
                default_index = 1,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
                    "icon": {"color": "black", "font-size": "23px"}, 
                    "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "navy-blue"},
                    "nav-link-selected": {"background-color": "white"},
                }
            )
        if app == "Homepage":
            Homepage.app()
        # # if app == "Books":
        # #     Books.app()    
        # # if app == "Podcast":
        # #     Podcast.app()        
        # # if app == "AudioBooks":
        # #     AudioBooks.app()
        # # if app == 'LoanBooks':
        # #     LoanBooks.app() 
    run()
        