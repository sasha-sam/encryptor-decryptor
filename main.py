import streamlit as st
from overview import display_overview
from utility import validate_registration
from register_authenticate import register, authenticate
from dashboard import display_dashboard

def main():

    '''
    The function handles the navigation accross multiple pages of the Streamlit application.
    Navigation Logic:
    - Checks if the 'page' key exists in 'st.session_state' object; if not sets it to 'overview'.
    - When the 'page' is set to 'overview', it displays the overview page.
    - If the 'Next' button is pressed, it check's the user's registration status.
        - If the user is unregistered, it navigates to the registration page.
        - If the user has registered, it directs the user to authentication page.
    - After successful registration or authentication, the user is directed to the main page of the application.
    '''
    
    # Checks if the 'page' key exists in session state; sets it to 'overview' if not found.
    if 'page' not in st.session_state:
        st.session_state.page = 'overview'
    if st.session_state.page == 'overview':
        display_overview()
        if st.button("Next"):
            # Reads the user's registration status from 'user_credentials.json' for navigation.
            registration_status = validate_registration()
            if registration_status == "Unregistered":
                st.session_state.page = 'register'
            elif registration_status == "Registered":
                st.session_state.page = 'authenticate'
    elif st.session_state.page == 'register':
        register()
    elif st.session_state.page == 'authenticate':
        authenticate()
    elif st.session_state.page == 'dashboard':
        display_dashboard()

if __name__ == "__main__":
    main()