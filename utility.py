import json
import bcrypt
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import datetime

def validate_registration() -> str:

    '''
    This function verifies the user's registration status for directing them accordingly:
    - Directs unregistered users to the registration page.
    - Directs registered users to the authentication page.
    '''

    # Loads the user's registration status from the json file.
    with open('user_credentials.json', 'r') as file:
        credentials = json.load(file)
    registration_status = credentials["Status"]
    return registration_status

def hash_password(password: str) -> str:

    '''
    This function hashes the password (passed as a parameter) using 'bcrypt' and returns the hashed password.
    '''

    # Generates a salt for additional security.
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_username(entered_username: str) -> bool:

    '''
    This function verifies the entered username against the registered user's stored username.
    '''

    with open('user_credentials.json', 'r') as file:
        credentials = json.load(file)
    stored_username = credentials["Username"]
    if entered_username == stored_username:
        return True
    else:
        return False

def verify_password(entered_password: str) -> bool:

    '''
    This function verifies the entered password against the registered user's stored hashed password.
    '''
    
    with open('user_credentials.json', 'r') as file:
        credentials = json.load(file)
    stored_hashed_password = credentials["Hashed Password"]
    # Checks if the hashed password is stored as a string.
    if isinstance(stored_hashed_password, str):
        # The entered password is first encoded to bytes and passed to 'checkpw' function, 'checkpw' applies the same hashing algorithm used for the stored password and if the entered password, when hashed, matches the stored hashed password, 'checkpw' returns True.
        return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
    
def generate_key() -> bytes:

    '''
    This function generates a 32-byte (256-bit) key using the operating system's random number generator.
    '''
    
    return os.urandom(32)

def bytes_to_hex(key: bytes) -> bytes:

    '''
    This function converts bytes to a base64-encoded string.
    '''
    
    return base64.b64encode(key).decode('utf-8')

def encrypt_file(data: bytes, key: bytes) -> tuple:

    '''
    Encrypts the given data using AES encryption algorithm with CBC mode.
    '''
    
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder =  padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

def save_file_metadata(file_name: str, hex_key: str) -> dict:

    '''
    Creates and returns metadata for a file.
    '''
    
    extension = os.path.splitext(file_name)[1]
    system_time = datetime.datetime.now().strftime("%d %m %Y %H:%M:%S")
    return {
        "File Name": file_name,
        "Extension": extension,
        "Encryption Key": hex_key,
        "Time": system_time
    }
    
def decrypt_file(encrypted_data: bytes, key: bytes) -> bytes:

    '''
    Decrypts the given data using AES encryption algorithm with CBC mode.
    '''
    
    iv = encrypted_data[:16]
    encrypted_content = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_content) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data

    
    

