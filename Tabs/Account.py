import streamlit as st


def app():
    st.title("Welcome to :blue[NIIE Library] 📚 ")
    option = st.selectbox("Select an option Login/Signup", ["Login", "Register"])
    if option == "Login":
        with st.form(key="Login Form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                st.write("Username: ", username)
                st.write("Password: ", password)
    else:
        with st.form(key="Register Form"):
            username = st.text_input("Username", placeholder="Username")
            email = st.text_input("Email", type="default", placeholder="Email")
            password = st.text_input("Password", type="password", placeholder="Password",
                                     help="Password must at least 8 characters")
            confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Confirm Password")
            submitted = st.form_submit_button("Register")
            if submitted:
                st.write("Username: ", username)
                st.write("Password: ", password)
                st.write("Confirm Password: ", confirm_pass)
                st.write("Email: ", email)


if __name__ == "__main__":
    app()
