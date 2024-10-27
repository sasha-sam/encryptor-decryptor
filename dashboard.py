import streamlit as st
from utility import generate_key, encrypt_file, save_file_metadata, decrypt_file
import json
import pandas as pd

def display_dashboard():
    '''
    Displays a dashboard for file encryption, decryption and key management.
    '''
    st.header("Dashboard")
    enc, dec, repository = st.tabs(["Encrypt", "Decrypt", "Key Repository"])
    if 'key_stored' not in st.session_state:
        st.session_state.key_stored = False
    with enc:
        uploaded_file = st.file_uploader("Choose a file to encrypt")
        if uploaded_file is not None and not st.session_state['key_stored']:
            file_content = uploaded_file.read()
            key = generate_key()
            hex_key = key.hex()
            st.write(f"generated file enc key: {hex_key}")
            file_name = uploaded_file.name
            try:
                with open('encryption_metadata.json', 'r') as file:
                    existing_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = {}
            file_key = f"File {len(existing_data) + 1}"
            existing_data[file_key] = save_file_metadata(file_name, hex_key)
            with open('encryption_metadata.json', 'w') as file:
                json.dump(existing_data, file, indent=4)
            st.session_state.key_stored = True
            encrypted_file = encrypt_file(file_content, key)
            st.download_button(
                label="Download encrypted file",
                data=encrypted_file,
                file_name=file_name,
            ) 
    with dec:
        uploaded_file = st.file_uploader("Choose a file to decrypt")
        if uploaded_file is not None:
            uploaded_file_content = uploaded_file.read()
            file_name = uploaded_file.name
            key_input = st.text_input("Enter the original encryption key", type = 'password')
            if key_input:
                try: 
                    key = bytes.fromhex(key_input)
                    with open('encryption_metadata.json', 'r') as file:
                        metadata = json.load(file)
                    for file_key, file_info in metadata.items():
                        if file_info["File Name"] == file_name and file_info["Encryption Key"] == key_input:
                            decrypted_file = decrypt_file(uploaded_file_content, key)
                            st.download_button(
                                label="Download decrypted file",
                                data=decrypted_file,
                                file_name=file_name
                            )
                except ValueError as e:
                    st.error(f"Invalid key :{e}")
                except Exception as e:
                    st.error(f"Decryption failed {e}")
    with repository:
        st.write("Here are the stored keys:")
        try:
            with open('encryption_metadata.json', 'r') as file:
                data = json.load(file)
            df = pd.DataFrame([{
                "File Name": i["File Name"],
                "Extension": i["Extension"],
                "Encryption Key": i["Encryption Key"],
                "Time": i["Time"]
            } for i in data.values()])
            df.index = range(1, (len(df) + 1))
            df.index.name = "File Number"
            st.table(df)
        except Exception as e:
            st.error(f"Error: {e}")