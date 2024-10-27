# Overview
This project is a single-user application built using Streamlit, designed for easy file encryption and decryption. It supports various file types, including text files, documents, images, media files, videos and code files.

## Key Features
- AES based encryption algorithm to ensure secure encryption and decryption of files.
- Automatic key generation and storage.

## Installation 
1. Install the necessary libraries:
    ```zsh
    pip install streamlit json bcrypt os base64 cryptography datetime
2. Clone this repository to your local machine.
4. Navigate to the project directory.
    ```zsh
    cd project_directory
3. Run the application using streamlit.
    ```zsh
    streamlit run main.py

## Usage
### How to encrypt a file?
1. On the main page of the application, navigate to the 'Encrypt' tab, where a file uploader will be available.
2. Choose any supported file from your machine.
3. Once a file is selected, a hex-key is generated. A download button appears, allowing you to download the encrypted file.
4. Store the hex-key securely, as it will be required for decryption.
### How to decrypt the encrypted file?
1. Go to 'Decrypt' tab and use the file uploader to upload the encrypted file.
2. After selecting the file, enter the hex-key.
3. If the correct key is entered, a download button appears, enabling you to retrieve the decrypted file.
### Hex-Key Recovery
If you forget to store the hex-key, you can access it from the 'Key Repository' tab on the main page.

## Future Improvements 
- Enable the application to support multiple users, each with their own unique encryption keys.
- Encrypt stored encryption keys so that the hex-keys are not visible even if the JSON file is accessed.

## Credits 
The folowing libraries are used to build the application:
- streamlit
- json
- bcrypt
- os
- base64
- cryptography
- datetime