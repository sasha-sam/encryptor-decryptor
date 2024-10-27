import streamlit as st

def display_overview():
    st.header(":green[File Encryptor-Decryptor]", divider="gray")
    st.subheader("Project Overview")
    st.write("This is a single-user Streamlit application that encrypts a file uploaded by the user using AES (Advanced Encryption Standard) encryption in CBC (Cipher Block Chaining) mode. This encryption method scrambles the file content into an unreadable format that can only be reversed using the correct decryption key.")
    st.subheader("How it works?")
    st.markdown("""
    1. **Encryption Process**: 
        - When the user uploads a file, the application generates a random 32-byte (256-bit) key. This key is used to encrypt the file.
        - A random initialization vector is generated to ensure each encryption is unique.
        - The file is split into blocks, and each block is encrypted sequentially, with each block's encryption depending on the encrypted data of the previous block.
        - Once the encryption is complete, the file is stored in its scrambled (encrypted) form, making it unreadable without the correct key and initialization vector.
    2. **Decryption Process**: 
        - To retrieve the original file, the user must provide the same encryption key used during the encryption process. 
        - The application reads the encrypted file and the associated initialization vector and using the correct key it decrypts the file block by block, reversing the encryption process.
        - After decryption, the original file is restored, and the user can access the content of the file. 
    """)
    st.subheader("Supported File Types")
    st.markdown("""
    - The application can encrypt and decrypt the following types of files: 
        - Text Files :gray-background[.txt], :gray-background[.csv]
        - Documents :gray-background[.docx], :gray-background[.pdf], :gray-background[.xlsx]
        - Images :gray-background[.jpg], :gray-background[.png], :gray-background[.gif]
        - Audio Files :gray-background[.mp3] 
        - Video Files :gray-background[.mp4]
        - Code Files :gray-background[.py], :gray-background[.js], :gray-background[.html]
    """)
    st.markdown("""
    **Note**: The application cannot fix or recover corrupted files. If a file is corrupted before encryption, it will remain corrupted after decryption. 
    """)
    st.subheader("Libraries Used")
    st.markdown("""
    - :gray-background[streamlit]: For creating the user-interface of the application.
    - :gray-background[json]: For reading and storing the data.
    - :gray-background[bcrypt]: For securely hashing user's password.
    - :gray-background[os]: For generating random bytes.
    - :gray-background[base64]: For encoding and decoding binary data. 
    - :gray-background[cryptography]: For designing the core encryption and decryption logic.
    - :gray-background[datetime]: For handling timestamps.
    """)