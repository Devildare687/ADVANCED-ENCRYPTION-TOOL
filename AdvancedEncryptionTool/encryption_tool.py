import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Define folder paths
ENCRYPTED_FOLDER = "encrypted_files"
DECRYPTED_FOLDER = "decrypted_files"

# Ensure folders exist
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Key-related functions
def generate_key():
    key = get_random_bytes(32)  # AES-256 requires a 32-byte key
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encryption function
def encrypt_file(input_file):
    key = load_key()
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, "rb") as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Save the encrypted file
    filename = os.path.basename(input_file)
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, f"{filename}.enc")
    with open(encrypted_path, "wb") as f:
        f.write(iv + ciphertext)
    
    print(f"File encrypted and saved to '{encrypted_path}'.")

# Decryption function
def decrypt_file(encrypted_file):
    key = load_key()
    with open(encrypted_file, "rb") as f:
        iv = f.read(16)  # AES block size
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Save the decrypted file
    filename = os.path.basename(encrypted_file).replace(".enc", "")
    decrypted_path = os.path.join(DECRYPTED_FOLDER, filename)
    with open(decrypted_path, "wb") as f:
        f.write(plaintext)

    print(f"File decrypted and saved to '{decrypted_path}'.")
