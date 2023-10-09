import streamlit as st
import json
import bcrypt


def authenticate():
    # Username and password input boxes
    username = st.text_input('Username', placeholder='Enter username')
    password = st.text_input('Password', placeholder='Enter password', type="password")
    
    # Login button
    if st.button('Login'):

        # Load all user from auth data file
        with open('data/users.json') as file:
            users = json.load(file)
        
        # Check if credentials are correct
        for user in users:
            if user["username"] == username:
                input_password = password.encode('utf8')
                user_password = user["password"].encode('utf-8')
                if bcrypt.checkpw(input_password, user_password):
                    st.write("Confirm login")
                    return True

        return False
