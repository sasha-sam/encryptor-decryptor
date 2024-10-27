import streamlit as st
from utility import hash_password, verify_username, verify_password
import json

def register():

    '''
    This function handles the user's registration process.
    '''

    if 'username' not in st.session_state:
        st.session_state['username'] = ""
    if 'password' not in st.session_state:
        st.session_state['password'] = ""
    st.header("Regsiter :bust_in_silhouette:")
    st.session_state['username'] = st.text_input("Create your username")
    username = st.session_state['username']
    if st.session_state["username"]:
        st.session_state['password'] = st.text_input("Create a password", type='password')
        password = st.session_state['password']
    if st.session_state['password']:
        if st.button('Register'):
            hashed_password = hash_password(password)
            # Saves the user's credentials in a json file.
            with open('user_credentials.json', 'w') as credentials:
                json.dump({"Username": username, "Hashed Password": hashed_password, "Status": "Registered"}, credentials, indent=4)
            st.session_state.page = 'dashboard'

def authenticate():
    
    '''
    This function handles the user's authentication process.
    '''

    if 'usernamme' not in st.session_state:
        st.session_state['username'] = ""
    if 'password' not in st.session_state:
        st.session_state['password'] = ""
    st.header("Authenticate :shield:")
    st.session_state['username'] = st.text_input("Enter you username")
    entered_username = st.session_state['username']
    if st.session_state['username']:
        st.session_state['password'] = st.text_input("Enter password", type='password')
        entered_password = st.session_state['password']
    if st.session_state['password']:
        if st.button('Authenticate'):
            # Verifies username and password using functions in 'utility.py'. 
            if verify_username(entered_username) and verify_password(entered_password):
                st.session_state.page = 'dashboard'
            else:
                st.error("Invalid username or password")    