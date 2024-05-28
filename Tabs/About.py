import streamlit as st

def app():

  
    
    # Header with color
    st.markdown("<h2 style='color:#2C3E50;'>Library Management System</h2>", unsafe_allow_html=True)
    
    # Smaller text for project details
    st.markdown("<p style='color:#2C3E50; font-size:16px;'>Final advanced programming project by Phung Gia Dat</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#2C3E50; font-size:16px;'>Built using Streamlit, MySQL, and Python</p>", unsafe_allow_html=True)
    
    # Features header and list
    st.markdown("<h3 style='color:#34495E;'>Features:</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="font-size:16px; color:#34495E;">
        <li>Add, update, delete, and view books</li>
        <li>User registration and sign-in</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Contact Information with Icons
    st.markdown("""
    ## Contact
    If you have any questions or feedback, feel free to reach out:
    - **Email**: <img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='20'/> [phunggiadat050904@gmail.com](mailto:phunggiadat050904@gmail.com)
    - **GitHub**: <img src='https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg' width='20'/> [Phung Gia Dat](https://github.com/PhungGiaDat/NIIE-Library-streamlit-)
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <style>
        .footer {
            color: #4A4A4A;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Created by Phung Gia Dat
    </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    app()
