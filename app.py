import streamlit as st
import home
import login

st.header('Kasada Calendar', divider='rainbow')

# Initialize auth session variable
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Check if user authentication
if not st.session_state.auth:
    # Render login page
    st.session_state.auth = login.authenticate()

else:
    # Add a logout button
    if st.button('Logout'):
        st.write("Logging out")
        st.session_state.auth = False
    
    # Render calendar component
    home.calendar_view()
